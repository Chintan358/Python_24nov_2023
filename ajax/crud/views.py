from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(request):
    print("hello")
    uname = request.POST['uname']
    email = request.POST['email']
    phone = request.POST['phone']
    age = request.POST['age']
    
    User.objects.create(username=uname,email=email,phone=phone,age=age)

    return HttpResponse("Registration success !!!")

def display(request):
    user_data  =User.objects.all()

    return JsonResponse({"data":list(user_data.values())})
