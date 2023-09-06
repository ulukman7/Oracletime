from django.db import models


class Office (models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    bluetooth = models.CharField(max_length=255)


class Employee (models.Model):
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
    end_time = models.DateTimeField(auto_now=True)


class Advance (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    advance = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Attendance (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="сотрудник")
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)


class Currency (models.Model):
    name = models.CharField(max_length=3)
    value = models.IntegerField()





