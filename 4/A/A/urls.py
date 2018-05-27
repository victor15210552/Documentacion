"""A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicacion.views import vista1A,vista2,vista3,vista4,vista5

urlpatterns = [
    path('admin/', admin.site.urls),

    path('vista1/', vista1A,name='vista1'),
    path('vista2/', vista2,name='vista1'),
    path('vista3/', vista3,name='vista1'),
    path('vista4/', vista4,name='vista1'),
    path('vista5/', vista5,name='vista1'),
]
