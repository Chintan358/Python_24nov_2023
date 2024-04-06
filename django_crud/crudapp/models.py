from django.db import models

# Create your models here.

class Emp(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    language=models.CharField(max_length=50)
    country=models.CharField(max_length=10)
    image = models.ImageField(upload_to="my_image",default="test")

