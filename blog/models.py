from django.db import models

class student(models.Model):
    name = models.CharField(max_length=200)
    rollNo = models.CharField(max_length=10)
    mobileNo = models.CharField(max_length=15)


# Create your models here.
