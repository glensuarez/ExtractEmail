"""
Definition of urls for ExtraccionCorreo.
"""


from django.urls import path
from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView
#from app import forms, views

#from AplicacionGlen.views import upload_document
from AplicacionGlen import views


urlpatterns = [
 
    path('admin/', admin.site.urls),

  
    path('', views.upload_document, name='upload_document')
]


