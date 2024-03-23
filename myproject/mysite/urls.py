from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('index',views.index,name="index"),
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact)
]