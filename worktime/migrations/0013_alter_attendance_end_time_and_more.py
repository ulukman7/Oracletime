# Generated by Django 4.2.5 on 2023-09-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0012_attendance_lateness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
