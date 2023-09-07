from django.contrib import admin
from .models import *
from .views import start_timer, stop_timer

# Register your models here.
admin.site.register(Office)
admin.site.register(Currency)
admin.site.register(Attendance)


class AdvanceInline(admin.TabularInline):
    model = Advance
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AdvanceInline]
    actions = [start_timer, stop_timer, ]
    list_display = ['first_name', 'salary', 'start_time', 'end_time', 'get_late_arrival',]

    def get_late_arrival(self, obj):
        late_arrival = obj.calculate_late_arrival()
        return str(late_arrival)

    get_late_arrival.short_description = 'Опоздание'

    def remaining_salary(self, obj):
        total_penalty = obj.penalty
        salary = obj.daily_salary
        remaining_salary = salary - total_penalty
        return remaining_salary

    remaining_salary.short_description = 'Оставшаяся зарплата'