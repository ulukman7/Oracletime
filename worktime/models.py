import datetime
from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    bluetooth = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=3)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    phone_id = models.IntegerField()
    salary = models.IntegerField()
    daily_salary = models.IntegerField()
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='employee')
    post = models.CharField(max_length=50)
    penalty = models.IntegerField()
    getting_started = models.TimeField(default='10:00:00')
    end_workday = models.TimeField(default='19:00:00')
    deadline = models.TimeField(default='16:00:00')

    def __str__(self):
        return self.first_name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='attendance', null=True, blank=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='office', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    arrival_time = models.TimeField(blank=True, null=True)
    care_time = models.TimeField(blank=True, null=True)
    lateness = models.IntegerField(null=True, blank=True, default=0)
    late_penalty = models.IntegerField(null=True, blank=True, )

    def calculate_lateness(self):
        if self.arrival_time and self.employee.getting_started:
            start_datetime = datetime.datetime.combine(self.date, self.arrival_time)
            default_start_time = datetime.datetime.combine(self.date, self.employee.getting_started)
            if start_datetime > default_start_time:
                lateness_timedelta = start_datetime - default_start_time
                lateness_minutes = int(lateness_timedelta.total_seconds() / 60)
                return lateness_minutes
        return 0
    calculate_lateness.short_description = 'Опоздание (минуты)'
    def late_penalty(self):
        late = int(self.calculate_lateness())
        penalty = self.employee.penalty
        late_penalty = penalty*late
        return late_penalty

    def penalty_salary(self):
        daily_salary = self.employee.daily_salary
        penalty = self.late_penalty()
        total_salary = daily_salary - penalty
        return total_salary

    def __str__(self):
        return str(self.id)


class Advance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    advance = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


