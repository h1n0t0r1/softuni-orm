import uuid
from datetime import datetime


from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save

from .fields import HexField, UnixTimestampField

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=10)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='employees')
    salary = models.IntegerField()
    department = models.CharField(max_length=50)
    hex_value = HexField()
    unix_timestamp = UnixTimestampField()
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')

    def clean(self):
        if self.salary < 3000:
            raise ValidationError('Salary must be at least 3000')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=30)




def post_saved(sender, instance, **kwargs):
    print(sender)
    print(instance.first_name, instance.last_name, instance.age, instance.gender)

post_save.connect(post_saved, sender=Employee)





