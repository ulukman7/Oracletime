import datetime
from datetime import timedelta,time,timezone

from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    bluetooth = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    phone_id = models.IntegerField()
    salary = models.IntegerField()
    daily_salary = models.IntegerField()
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='офис')
    post = models.CharField(max_length=50)
    penalty = models.IntegerField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    def calculate_late_arrival(self):
        late_arrival_time = datetime.time(4)
        start_time = self.start_time.time()

        if start_time > late_arrival_time:
            late_hours = start_time.hour - late_arrival_time.hour
            late_minutes = start_time.minute - late_arrival_time.minute
            return f"{late_hours} часов {late_minutes} минут"
        else:
            return "Без опоздания"



    def __str__(self):
        return self.first_name

    def get_attendances(self):
        return self.attendance_set.order_by('date')

class Advance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    advance = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="сотрудник")
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time_default = models.DateTimeField()
    end_time_default = models.DateTimeField()

    def calculate_late_arrival(self):
        late_arrival_time = datetime.time(10, 0)  # Время начала работы, 10:00

        # Убедитесь, что start_time_default и start_time имеют совместимые форматы
        if self.start_time_default and self.start_time:
            late_duration = self.start_time_default - self.start_time
            return late_duration
        else:
            return timedelta(0)
    def __str__(self):
        return str(self.employee)

class Currency(models.Model):
    name = models.CharField(max_length=3)
    value = models.IntegerField()

    def __str__(self):
        return self.name
