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
        # Здесь мы создаем ссылку на аттенданс сотрудника по его имени
        url = reverse('admin:worktime_attendance_changelist') + f'?employee__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, obj.first_name)


#
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee_link', 'office', 'employee_daily_salary', 'date', 'start_time', 'end_time', 'calculate_lateness', 'late_penalty', 'penalty_salary',]
    list_filter = ('date',)
    actions = [view_attendance]

    def employee_link(self, obj):
        # Здесь мы создаем ссылку на страницу редактирования сотрудника по его имени
        url = reverse('admin:worktime_employee_change', args=[obj.employee.id])
        return format_html('<a href="{}">{}</a>', url, obj.employee.first_name)
    def employee_daily_salary(self, obj):
        return obj.employee.daily_salary
    def employee_name(self, obj):
        return obj.employee.first_name



    # def calculate_late(self, obj):
    #     employee = obj.employee
    #     return employee.calculate_late_arrival(obj)

    # def calculate_remaining_salary(self, obj):
    #     if obj.Employee:
    #         total_penalty = obj.Employee.penalty
    #         salary = obj.Employee.daily_salary
    #         remaining_salary = salary - total_penalty
    #         return remaining_salary
    #     return "N/A"  # Handle the case where there's no related employee
    #
    # calculate_remaining_salary.short_description = 'Оставшаяся зарплата'

