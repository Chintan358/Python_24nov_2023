from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    age = models.IntegerField()