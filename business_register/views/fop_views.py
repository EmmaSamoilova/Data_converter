from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from business_register.filters import FopFilterSet
from business_register.models.fop_models import Fop
from business_register.serializers.fop_serializers import FopSerializer
from data_converter.pagination import CachedCountPagination
from data_ocean.filters import FullWordSearchFilter
from data_ocean.permissions import IsAuthenticatedAndPaidSubscription
from data_ocean.tasks import export_to_s3
from data_ocean.views import CachedViewSetMixin, RegisterViewMixin


@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['business register']))
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['business register']))
@method_decorator(name='export_to_xlsx', decorator=swagger_auto_schema(auto_schema=None))
class FopViewSet(RegisterViewMixin,
                 CachedViewSetMixin,
                 viewsets.ReadOnlyModelViewSet):
    pagination_class = CachedCountPagination
    queryset = Fop.objects.select_related(
        'status', 'authority'
    ).prefetch_related(
        'kveds', 'exchange_data'
    ).all()
    filter_backends = (DjangoFilterBackend, FullWordSearchFilter)
    serializer_class = FopSerializer
    filterset_class = FopFilterSet
    search_fields = ('fullname', 'address', 'status__name')

    @action(detail=False, url_path='xlsx', permission_classes=[IsAuthenticatedAndPaidSubscription])
    def export_to_xlsx(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset.count() > settings.FOP_TO_XLSX_LIMIT:
            return Response(
                {"detail": _("Too many results for export in .xlsx. Try reduce filter conditions.")},
                status=416
            )
        export_dict = {
            'ID': ['pk', 9],
            'Full Name': ['fullname', 30],
            'Status': ['status', 14],
            'Address': ['address', 33],
            'Registration Date': ['registration_date', 18],
            'Termination Date': ['termination_date', 18],
            'Created Date': ['created_at', 19],
            'Updated Date': ['updated_at', 19],
            'Authority': ['authority', 36]
        }
        export_to_s3.delay(request.GET, export_dict, 'business_register.Fop',
                           'business_register.filters.FopFilterSet', request.user.id)
        return Response(
            {"detail": _("Generation of .xlsx file has begin. Expect an email with downloading link.")},
            status=200
        )
