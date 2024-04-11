from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
# Create your views here.

@api_view(['get'])
def viewdata(request):
    user_data = User.objects.all()
    ser_data =  UserSerializer(user_data,many=True)
    return Response({'data':ser_data.data})

@api_view(['post'])
def adddata(request):

    print(request.data)
    ser_data =  UserSerializer(data=request.data)
    if not ser_data.is_valid():
        return Response({"message":"something went wrong","errors":ser_data.errors})
    ser_data.save()
    return Response({"userdata":ser_data.data,"message":"User inserted"})

@api_view(['put'])
def updatedata(request,id):
    try:
        user_data = User.objects.get(id=id)
        ser_data = UserSerializer(user_data,request.data)
        if not ser_data.is_valid():
            return Response({"message":"something went wrong","errors":ser_data.errors})
        ser_data.save()
        return Response({"userdata":ser_data.data,"message":"User Updated"})
    except Exception as e:
        print(e)
        return Response({"Error":"Id not found"})
    
@api_view(['delete'])
def deletedata(request,id):
    try:
        user_data = User.objects.get(id=id)
        user_data.delete()
        return Response({"message":"data deleted"})
    except Exception as e:
        print(e)
        return Response({"Error":"Id not found"})