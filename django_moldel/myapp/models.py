from django.db import models

# Create your models here.
class Department(models.Model):
    deptname = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.deptname

class Employee(models.Model):
    Department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    salary = models.IntegerField()
    age = models.IntegerField(default=0)