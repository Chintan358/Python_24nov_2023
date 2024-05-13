from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(request):
   
    uname = request.POST['uname']
    email = request.POST['email']
    phone = request.POST['phone']
    age = request.POST['age']
    
    User.objects.create(username=uname,email=email,phone=phone,age=age)

    return HttpResponse("Registration success !!!")

def display(request):
    user_data  =User.objects.all()

    return JsonResponse({"data":list(user_data.values())})

def delete(request):
    if request.method=="GET":
        id=request.GET.get('id')
        userdata=User.objects.get(pk=id)
        userdata.delete()
    else:
        return HttpResponse("somthigs went wrong")

    return HttpResponse("delete successfull !!!")

def edit(request):
    if request.method == 'GET':
        id=request.GET.get('id')
        userdata=User.objects.filter(pk=id)
    return JsonResponse({"data":list(userdata.values())})
   

def update(request):

    pk=request.POST['id']
    udata = User.objects.get(id=pk)
    
    udata.username = request.POST['uname']
    udata.email = request.POST['email']
    udata.phone = request.POST['phone']
    udata.age = request.POST['age']
    udata.save()
    return HttpResponse("User updated")


def search(request):
    dt = request.GET.get('dt')
    user_data  =User.objects.filter(
        
        Q(username__startswith=dt) |
        Q(email__startswith=dt) |
        Q(phone__startswith=dt) |
        Q(age__startswith=dt) 
        
        )

    return JsonResponse({"data":list(user_data.values())})