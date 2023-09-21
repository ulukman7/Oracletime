# Generated by Django 4.2.5 on 2023-09-18 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0004_alter_attendance_end_time_default_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='employees',
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='посещение', to='worktime.employee'),
        ),
        migrations.AlterField(
            model_name='advance',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='worktime.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='end_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
