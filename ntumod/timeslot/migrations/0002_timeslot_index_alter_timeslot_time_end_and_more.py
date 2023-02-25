# Generated by Django 4.1 on 2023-02-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timeslot", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="timeslot",
            name="index",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="time_end",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="time_start",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
