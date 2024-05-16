
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("shop/",shop,name="shop"),
    path("shopdetails/",shopdetails,name="shopdetails"),
    path("contact/",contact,name="contact"),
    path("cart/",cart,name="cart")

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)