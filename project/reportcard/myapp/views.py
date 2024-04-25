from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    studen_data = Student.objects.all()

    return render(request,"index.html",{"sdata":studen_data})