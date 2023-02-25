# Generated by Django 4.0.4 on 2023-02-25 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venue', '0001_initial'),
        ('course_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('group', models.CharField(blank=True, max_length=10, null=True)),
                ('day', models.CharField(blank=True, max_length=4, null=True)),
                ('time_start', models.DateTimeField(blank=True, null=True)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course_module.module')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='venue.venue')),
            ],
        ),
    ]
