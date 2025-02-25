from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=40)
    salary = models.IntegerField()
    department = models.CharField(max_length=50)