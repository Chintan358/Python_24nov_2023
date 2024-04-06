from django.contrib import admin
from django.urls import path
from crudapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.loginpage,name="login"),
    path("reg",views.regpage,name="reg"),
    path('index',views.index,name="index"),
    path('delete/<id>',views.delete,name="delete"),
    path('edit/<id>',views.edit,name="edit"),
    path("logout",views.logoutpage,name="logout")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)