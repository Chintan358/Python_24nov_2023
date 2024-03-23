from django.shortcuts import render,redirect
from .models import*

# Create your views here.

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