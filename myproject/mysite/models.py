from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password=models.CharField(max_length=50)

  

class Product(models.Model):
    productname=models.CharField(max_length=10)
    price=models.IntegerField()
    qty=models.IntegerField()