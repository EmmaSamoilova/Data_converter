# Generated by Django 3.0.7 on 2021-04-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0082_auto_20210414_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fop',
            name='vp_dates',
            field=models.CharField(blank=True, max_length=340, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfop',
            name='vp_dates',
            field=models.CharField(blank=True, max_length=340, null=True),
        ),
    ]
