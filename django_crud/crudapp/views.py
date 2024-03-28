from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def index(request):

        if request.method=='POST':
            data = request.POST
            uname = data.get('uname')
            email = data.get('email')
            password=data.get('password')
            gender=data.get('gender')
            language=data.getlist('lang')
            country=data.get('country')
            
            lng=""
            for i in language:
                lng = lng+i+","
            
            Emp.objects.create(username=uname,email=email,password=password,gender=gender,language=lng,country=country)

        alldata = Emp.objects.all
        return render(request,'index.html',{"empdata":alldata})

@login_required(login_url="/")
def delete(request,id):
    edata =  Emp.objects.get(id=id)
    edata.delete()
    return redirect('/')

def edit(request,id):
    edata =  Emp.objects.get(id=id)
    if request.method=='POST':
            data = request.POST
            edata.username = data.get('uname')
            edata.email = data.get('email')
            edata.password=data.get('password')
            edata.gender=data.get('gender')
            language=data.getlist('lang')
            edata.country=data.get('country')
            
            lng=""
            for i in language:
                lng = lng+i+","

            edata.language=lng
            edata.save()
            return redirect('/')

    return render(request,'update.html',{"edata":edata})

def loginpage(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get("uname")
        password = data.get("password")

        if not User.objects.filter(username=uname).exists():
            messages.info(request,"Invalid credentials")
            return redirect("/")
        
        user = authenticate(username=uname,password=password)
        if user is None:
            messages.info(request,"Invalid credentials")
            return redirect("/")
        else:
            login(request,user)
            return redirect("index")
        
    return render(request,"login.html")

def regpage(request):
     
     if request.method=='POST':
          data = request.POST
          fname = data.get("fname")
          lname = data.get("lname")
          uname = data.get("uname")
          password = data.get("password")

          if User.objects.filter(username=uname).exists():
            messages.info(request,"Username exists !!!")
            return redirect("reg")

          else:
            user =  User.objects.create(first_name=fname,last_name=lname,username=uname)
            user.set_password(password)
            user.save()
            messages.info(request,"Registration successfully !!!")
            return redirect("reg")

     return render(request,"registration.html")

def logoutpage(request):
    logout(request)
    return render(request,"login.html")