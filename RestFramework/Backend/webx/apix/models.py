from secrets import choice
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=3, choice=(
        ('M', "Male"), ('F', "Female"), ('O', "Others`")))
