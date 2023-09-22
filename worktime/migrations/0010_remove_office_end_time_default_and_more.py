# Generated by Django 4.2.5 on 2023-09-21 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0009_alter_attendance_office_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='end_time_default',
        ),
        migrations.RemoveField(
            model_name='office',
            name='start_time_default',
        ),
        migrations.AddField(
            model_name='employee',
            name='end_time_default',
            field=models.TimeField(blank=True, default='19:00:00', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='start_time_default',
            field=models.TimeField(blank=True, default='10:00:00', null=True),
        ),
    ]
