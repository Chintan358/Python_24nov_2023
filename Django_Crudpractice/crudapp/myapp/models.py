from django.db import models

# Create your models here.
class Student(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
