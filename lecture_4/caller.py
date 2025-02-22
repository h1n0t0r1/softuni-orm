import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Employee, Student
from django.db import connection, reset_queries
# Run and print your queries


def get_students_info():
    all_students = Student.objects.all()
    return '\n'.join(f"Student №{s.student_id}: {s.first_name} {s.last_name}; Email: {s.email}" for s in all_students)


def add_students():

    student_1 = Student(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )
    student_1.save()

    student_2 = Student(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )
    student_2.save()

    student_3 = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )
    student_3.save()

    student_4 = Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )
    student_4.save()


def update_students_emails():
    all_students = Student.objects.all()
    for s in all_students:
        s.email = s.email.replace(s.email.split('@')[1], 'uni-students.com')
        s.save()


def truncate_students():
    Student.objects.all().delete()


