import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Student, Subject, StudentEnrollment

# Create queries within functions

subject = Subject.objects.first()
studentenrollment = subject.studentenrollments_set.all()
