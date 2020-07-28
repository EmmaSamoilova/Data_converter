from django_filters import rest_framework as filters
from .models.company_models import Company
from .models.fop_models import Fop

from .models.kved_models import Kved


class CompanyFilterSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = {
            'edrpou': ['exact'],
        }


class FopFilterSet(filters.FilterSet):
    fullname = filters.CharFilter(lookup_expr='iexact')
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Fop
        fields = {
            'status': ['exact'],
            'registration_date': ['exact', 'lt', 'gt'],
            'termination_date': ['exact', 'lt', 'gt'],
            'authority': ['exact']
        }


class KvedFilterSet(filters.FilterSet):
    code = filters.CharFilter(lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains')

    o = filters.OrderingFilter(
        fields=(
            ('code', 'code'),
            ('name', 'name'),
            ('group__name', 'group'),
            ('division__name', 'division'),
            ('section__name', 'section'),
        ),
    )

    class Meta:
        model = Kved
        fields = ()