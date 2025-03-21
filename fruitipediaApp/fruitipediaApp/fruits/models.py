from django.core.validators import MinLengthValidator
from django.db import models
from .validators import  only_letters_validator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator
        ]

    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='fruits',
        null=True,
        blank=True
    )