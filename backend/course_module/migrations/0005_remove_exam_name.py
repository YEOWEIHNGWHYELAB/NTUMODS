# Generated by Django 4.1.6 on 2023-02-25 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0004_exam_name_alter_module_module_prereq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='name',
        ),
    ]
