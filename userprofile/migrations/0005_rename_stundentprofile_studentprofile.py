# Generated by Django 4.2.4 on 2023-08-20 11:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faculty', '0002_rename_semister_subject_semester'),
        ('userprofile', '0004_alter_stundentprofile_parents_contact_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StundentProfile',
            new_name='StudentProfile',
        ),
    ]
