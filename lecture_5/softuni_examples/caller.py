import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "softuni_examples.settings")
django.setup()

# Import your models here
from employees.models import Employee
from django.db import connection, reset_queries
from django.db.models import F

# Run and print your queries
# Employee.objects.update(salary=F('salary') * 1.1)

Employee.objects.filter(department='Marketing').update(salary=F('salary') * 1.05)

