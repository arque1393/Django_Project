
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=40, unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=30, choices=(
        ('M', "Male"), ('F', "Female"), ('O', "Others`")))

    @property
    def get_number(self):
        return 265296
