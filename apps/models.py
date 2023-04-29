import uuid

from django.db import models
from django.db.models import TextChoices


class Car(models.Model):
    class Type(TextChoices):
        SEDAN = 1, 'Sedan'
        TRUCK = 2, 'Truck'
        SUV = 4, 'SUV'

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=24, choices=Type.choices, blank=True, null=True)


class Event(models.Model):
    details = models.TextField()
    years_ago = models.PositiveIntegerField()
