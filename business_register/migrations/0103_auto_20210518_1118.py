# Generated by Django 3.1.8 on 2021-05-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0102_auto_20210514_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='luxuryitemright',
            name='additional_info',
            field=models.TextField(blank=True, default='', help_text='additional info about the right', verbose_name='additional info'),
        ),
        migrations.AddField(
            model_name='propertyright',
            name='additional_info',
            field=models.TextField(blank=True, default='', help_text='additional info about the right', verbose_name='additional info'),
        ),
        migrations.AddField(
            model_name='securitiesright',
            name='additional_info',
            field=models.TextField(blank=True, default='', help_text='additional info about the right', verbose_name='additional info'),
        ),
        migrations.AddField(
            model_name='vehicleright',
            name='additional_info',
            field=models.TextField(blank=True, default='', help_text='additional info about the right', verbose_name='additional info'),
        ),
        migrations.AlterField(
            model_name='luxuryitemright',
            name='share',
            field=models.FloatField(blank=True, help_text='share of the right', null=True, verbose_name='share of the right'),
        ),
        migrations.AlterField(
            model_name='luxuryitemright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (7, 'Other right of usage'), (10, 'Owner is another person'), (11, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='propertyright',
            name='share',
            field=models.FloatField(blank=True, help_text='share of the right', null=True, verbose_name='share of the right'),
        ),
        migrations.AlterField(
            model_name='propertyright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (7, 'Other right of usage'), (10, 'Owner is another person'), (11, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='securitiesright',
            name='share',
            field=models.FloatField(blank=True, help_text='share of the right', null=True, verbose_name='share of the right'),
        ),
        migrations.AlterField(
            model_name='securitiesright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (7, 'Other right of usage'), (10, 'Owner is another person'), (11, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='vehicleright',
            name='share',
            field=models.FloatField(blank=True, help_text='share of the right', null=True, verbose_name='share of the right'),
        ),
        migrations.AlterField(
            model_name='vehicleright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (7, 'Other right of usage'), (10, 'Owner is another person'), (11, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
    ]
