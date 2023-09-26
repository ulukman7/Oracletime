
from .models import Attendance
from django.utils import timezone
import pytz


def start_timer(modeladmin, request, queryset):
    now = timezone.now()
    tz = pytz.timezone('Asia/Bishkek')
    now = now.astimezone(tz)
    for employee in queryset:
        office = employee.office
        new_attendance = Attendance(employee=employee, office=office, date=now.date(), arrival_time=now, )
        new_attendance.save()
    modeladmin.message_user(request, f"Созданы записи Attendance для {queryset.count()} сотрудников с начальным временем.")
start_timer.short_description = "Начать отсчет времени"


def stop_timer(modeladmin, request, queryset):
    attendances = Attendance.objects.filter(id__in=queryset.values_list('id'))
    now = timezone.now()
    for attendance in attendances:
        attendance.care_time = now
        attendance.save()


    modeladmin.message_user(request, f"Время для {queryset.count()} записей было остановлено.")






