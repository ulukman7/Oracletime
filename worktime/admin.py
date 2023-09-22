from django.contrib import admin
from .models import Attendance, Employee, Office, Advance , Currency
from .views import start_timer, stop_timer, view_attendance
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
admin.site.register(Office)
admin.site.register(Currency)


class AdvanceInline(admin.TabularInline):
    model = Advance
    extra = 00


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AdvanceInline]
    actions = [view_attendance, start_timer, stop_timer, ]
    list_display = ['employee_link',  'salary', 'daily_salary', 'office', 'post',]

    def employee_link(self, obj):
        url = reverse('admin:worktime_attendance_changelist') + f'?employee__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, obj.first_name)


#
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee_link', 'office', 'employee_daily_salary', 'date', 'start_time', 'end_time', 'calculate_lateness', 'late_penalty', 'penalty_salary', ]
    list_filter = ('date',)


    def employee_link(self, obj):
        url = reverse('admin:worktime_employee_change', args=[obj.employee.id])
        return format_html('<a href="{}">{}</a>', url, obj.employee.first_name)


    def employee_daily_salary(self, obj):
        return obj.employee.daily_salary

    def employee_name(self, obj):
        return obj.employee.first_name





