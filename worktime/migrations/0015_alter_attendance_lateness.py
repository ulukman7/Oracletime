# Generated by Django 4.2.5 on 2023-09-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0014_rename_end_time_attendance_arrival_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='lateness',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
