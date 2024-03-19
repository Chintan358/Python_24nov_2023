from django.shortcuts import render,HttpResponse
from .models import Student
from django.contrib import messages
# Create your views here.
def index(request):
     
     if request.method=='POST':
          data = request.POST
          uname = data.get('uname')
          email = data.get('email')
          password=data.get('password')

          Student.objects.create(name=uname,email=email,password=password)

     messages.success(request,"Registration sucessfully done !!!")
     return render(request,'index.html')

def home(request):
     # conext = {"data":"Hello python"}

     std = [{"name":"Maulik","email":"maulik@gmail.com", "phone":"9685748596"},{"name":"Priyansh","email":"priyansh@gmail.com", "phone":"9685748596"},{"name":"Akshay","email":"akshay@gmail.com", "phone":"9685748566"}]
     
     return render(request,'home.html',{'stddata':std})

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')
