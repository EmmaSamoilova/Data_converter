# Generated by Django 2.0.9 on 2020-03-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratu', '0007_auto_20200331_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfop',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='rfop',
            name='fullname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rfop',
            name='kved',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='rfop',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]