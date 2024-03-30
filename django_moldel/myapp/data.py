from faker import Faker
fake =Faker()
from .models import *
import random

def getData(n=10):
   for i in range(0,n):
     alldept = Department.objects.all()
     num = random.randint(0,len(alldept)-1)
     dept = alldept[num]
     name = fake.name()
     email=fake.email()
     salary = random.randint(10000,99999)

     Employee.objects.create(Department=dept, name=name,email=email,salary=salary)