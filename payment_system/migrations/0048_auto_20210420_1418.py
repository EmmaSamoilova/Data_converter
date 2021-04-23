# Generated by Django 3.1.8 on 2021-04-20 14:18

from django.db import migrations


def set_invoice_data(apps, schema):
    Invoice = apps.get_model('payment_system', 'Invoice')
    for invoice in Invoice.objects.all():
        owner = invoice.project_subscription.project.owner

        invoice.email = owner.email
        invoice.full_name = f'{owner.first_name} {owner.last_name}'
        invoice.iban = owner.iban
        invoice.person_status = owner.person_status
        invoice.company_address = owner.company_address
        invoice.identification_code = owner.identification_code
        invoice.mfo = owner.mfo
        invoice.company_name = owner.company_name
        invoice.save()


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0047_auto_20210419_1548'),
    ]

    operations = [
        migrations.RunPython(
            code=set_invoice_data,
            reverse_code=migrations.RunPython.noop,
        )
    ]