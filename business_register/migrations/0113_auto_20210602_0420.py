# Generated by Django 3.1.8 on 2021-06-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0112_merge_20210601_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declaration',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='declaration',
            name='submission_date',
            field=models.DateField(blank=True, help_text='date of submission of the declaration', null=True, verbose_name='submission date'),
        ),
    ]
