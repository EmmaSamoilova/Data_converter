# Generated by Django 3.1.8 on 2021-05-26 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0106_auto_20210525_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companysanction',
            old_name='name_original_transcription',
            new_name='name_original',
        ),
        migrations.RenameField(
            model_name='personsanction',
            old_name='full_name_original_transcription',
            new_name='full_name_original',
        ),
    ]
