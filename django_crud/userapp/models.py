from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import *
from django.contrib.auth.models import User
class CustomeUser(AbstractUser):

    username = None
    phone_number = models.CharField(max_length=20,unique=True)
    user_info = models.CharField(max_length=50)

    USERNAME_FIELD = "phone_number"
    objects = UserManager()
