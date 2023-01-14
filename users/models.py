from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=10,null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll_no=models.IntegerField()