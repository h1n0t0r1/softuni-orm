from django.urls import path
from .views import employee_list

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
]
