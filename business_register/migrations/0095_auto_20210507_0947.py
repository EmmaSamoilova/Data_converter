# Generated by Django 3.0.7 on 2021-05-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0094_auto_20210430_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact_info',
            field=models.TextField(help_text='Info about contacts', null=True, verbose_name='contacts'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='address',
            field=models.TextField(blank=True, default='', help_text='Founder address in Ukrainian', null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='info',
            field=models.TextField(help_text='Info', verbose_name='info'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='info_additional',
            field=models.TextField(help_text='Additional info', null=True, verbose_name='additional info'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='info_beneficiary',
            field=models.TextField(help_text='Beneficiary Info', null=True, verbose_name='beneficiary info'),
        ),
        migrations.AlterField(
            model_name='historicalcompany',
            name='contact_info',
            field=models.TextField(help_text='Info about contacts', null=True, verbose_name='contacts'),
        ),
        migrations.AlterField(
            model_name='historicalfounder',
            name='address',
            field=models.TextField(blank=True, default='', help_text='Founder address in Ukrainian', null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='historicalfounder',
            name='info',
            field=models.TextField(help_text='Info', verbose_name='info'),
        ),
        migrations.AlterField(
            model_name='historicalfounder',
            name='info_additional',
            field=models.TextField(help_text='Additional info', null=True, verbose_name='additional info'),
        ),
        migrations.AlterField(
            model_name='historicalfounder',
            name='info_beneficiary',
            field=models.TextField(help_text='Beneficiary Info', null=True, verbose_name='beneficiary info'),
        ),
    ]
