# Generated by Django 3.1.8 on 2021-05-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0096_auto_20210511_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaration',
            name='nacp_declarant_id',
            field=models.PositiveBigIntegerField(db_index=True, verbose_name='NACP id of the declarant'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='nacp_id',
            field=models.PositiveBigIntegerField(blank=True, db_index=True, help_text='id from the National agency on corruption prevention', null=True, verbose_name='id from NACP'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='nacp_id',
            field=models.PositiveBigIntegerField(blank=True, help_text='id from the National agency on corruption prevention', null=True, unique=True, verbose_name='id from NACP'),
        ),
    ]