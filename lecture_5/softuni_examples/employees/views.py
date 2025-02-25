from django.shortcuts import render

from employees.models import Employee
from django.db.models import Q, F


# Create your views here.
def employee_list(request):
    employees = Employee.objects.filter(department='Marketing')

    return render(request, 'employees\employees.html', {'employees': employees})