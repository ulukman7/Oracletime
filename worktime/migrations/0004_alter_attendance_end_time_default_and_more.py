# Generated by Django 4.2.5 on 2023-09-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0003_remove_employee_attendance_attendance_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='end_time_default',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='start_time_default',
            field=models.TimeField(),
        ),
    ]