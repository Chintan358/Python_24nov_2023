from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get('uname')
        email = data.get('email')
        password = data.get('password')
        
        Student.objects.create(uname=uname,email=email,password=password)
        return redirect("/")

    sdata = Student.objects.all()
    return render(request,'index.html',{'sdata':sdata})

def delete(request,id):
    alldata = Student.objects.get(id=id)
    alldata.delete()
    return redirect("/")

def edit(request,id):
    alldata = Student.objects.get(id=id)
    if request.method=='POST':
        data = request.POST
        alldata.uname = data.get('uname')
        alldata.email = data.get('email')
        alldata.password = data.get('password')
        alldata.save()
        return redirect("/")
    
    return render(request,'update.html',{'sdata':alldata})
