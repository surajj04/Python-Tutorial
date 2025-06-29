from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    marks = models.FloatField(max_length=100)
    active = models.BooleanField(default=False)
