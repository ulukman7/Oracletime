
from .models import Attendance, Office, Employee
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
import pytz




def view_attendance(self, request, queryset):
    if queryset.count() == 1:
        employee = queryset.first()
        url = reverse('admin:worktime_attendance_changelist') + f'?employee__id__exact={employee.id}'
        return HttpResponseRedirect(url)
    else:
        self.message_user(request, "Select only one employee to view attendance.", level='warning')


view_attendance.short_description = "View Attendance"

def start_timer(modeladmin, request, queryset):
    now = timezone.now()
    tz = pytz.timezone('Asia/Bishkek')
    now = now.astimezone(tz)
    for employee in queryset:
        office = employee.office
        new_attendance = Attendance(employee=employee, office=office, date=now.date(), start_time=now, end_time=now)
        new_attendance.save()
    modeladmin.message_user(request, f"Созданы записи Attendance для {queryset.count()} сотрудников с начальным временем.")
start_timer.short_description = "Начать отсчет времени"


def stop_timer(modeladmin, request, queryset):
    now = timezone.now()
    for attendance in queryset:
        attendance.end_time = now
        attendance.save()
    modeladmin.message_user(request, f"Время для {queryset.count()} записей было остановлено.")

stop_timer.short_description = "Остановить время"




