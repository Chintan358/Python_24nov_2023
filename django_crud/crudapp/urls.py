from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path("",views.loginpage,name="login"),
    path("reg",views.regpage,name="reg"),
    path('index',views.index,name="index"),
    path('delete/<id>',views.delete,name="delete"),
    path('edit/<id>',views.edit,name="edit"),
    path("logout",views.logoutpage,name="logout")
]