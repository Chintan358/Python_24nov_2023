from django.contrib import admin
from .models import Emp
# Register your models here.

class EmpView(admin.ModelAdmin):
    list_display = ['username',"email","password","gender",'language','country','image']


admin.site.register(Emp,EmpView)