# Generated by Django 3.1.12 on 2021-07-05 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0141_merge_20210705_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporaterightsright',
            name='company_name',
            field=models.TextField(blank=True, default='', help_text='name of the company that owns the right', verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='luxuryitemright',
            name='company_name',
            field=models.TextField(blank=True, default='', help_text='name of the company that owns the right', verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='pepscoring',
            name='declaration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scoring', to='business_register.declaration'),
        ),
        migrations.AlterField(
            model_name='propertyright',
            name='company_name',
            field=models.TextField(blank=True, default='', help_text='name of the company that owns the right', verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='securitiesright',
            name='company_name',
            field=models.TextField(blank=True, default='', help_text='name of the company that owns the right', verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='vehicleright',
            name='company_name',
            field=models.TextField(blank=True, default='', help_text='name of the company that owns the right', verbose_name='company name'),
        ),
        migrations.AlterUniqueTogether(
            name='pepscoring',
            unique_together={('declaration', 'rule_id')},
        ),
    ]