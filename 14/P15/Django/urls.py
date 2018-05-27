"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app import views
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/', login, {'template_name': 'app/login.html'}, name = 'login'),
    url(r'logout/', logout_then_login, name="logout"),

    url('formulario_Alumno/', views.formulario_Alumno.as_view(), name = 'formulario_Alumno'),
    url('formulario_Mestro/', views.formulario_Mestro.as_view(), name = 'formulario_Mestro'),
    url('formulario_Clase/', views.formulario_Clase.as_view(), name = 'formulario_Clase'),
    url('formulario_Horario/', views.formulario_Horario.as_view(), name = 'formulario_Horario'),
    url('formularo_Carrera/', views.formularo_Carrera.as_view(), name = 'formularo_Carrera'),
]
