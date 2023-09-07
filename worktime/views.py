
from .models import *
from django.utils import timezone

def start_timer(modeladmin, request, queryset):
    now = timezone.now()
    for attendance in queryset:
        attendance.start_time = now
        attendance.end_time = now
        attendance.save()
    modeladmin.message_user(request, f"Начат отсчет времени для {queryset.count()} записей.")
start_timer.short_description = "Начать отсчет времени"

def stop_timer(modeladmin, request, queryset):
    now = timezone.now()
    for attendance in queryset:
        attendance.end_time = now
        attendance.save()
    modeladmin.message_user(request, f"Время для {queryset.count()} записей было остановлено.")

stop_timer.short_description = "Остановить время"