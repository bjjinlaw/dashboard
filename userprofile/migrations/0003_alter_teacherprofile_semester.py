# Generated by Django 4.2.4 on 2023-08-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_rename_semister_subject_semester'),
        ('userprofile', '0002_alter_teacherprofile_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='semester',
            field=models.ManyToManyField(related_name='teacher_semester', to='faculty.semester'),
        ),
    ]
