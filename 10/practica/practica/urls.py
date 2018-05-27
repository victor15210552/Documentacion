"""practica URL Configuration

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
from app.views import Persona,Heroe,Boxeador,DragonBall,Ninja,Capitan,Equipo,ExamenChunin,reporte_Ninja,reporte_Heroe,reporte_Boxeador,reporte_DragonBall,reporte_Persona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Ninja/', Ninja,name='Ninja_view'),
    path('Capitan/', Capitan, name= 'Capitan_view'),
    path('Equipo/', Equipo, name='Equipo_view'),
    path('ExamenChunin/', ExamenChunin, name='ExamenChunin_view'),
    path('Persona/', Persona, name= 'Persona_view'),
    path('Heroe/', Heroe, name= 'Heroe_view'),
    path('Boxeador/', Boxeador, name= 'Boxeador_view'),
    path('DragonBall/', DragonBall, name= 'DragonBall_view'),
#-------- URL DEL REPORTE---------
    
    path('reporte_Ninja/', reporte_Ninja, name= 'reporte_Ninja_view'),
    path('reporte_Heroe/', reporte_Heroe, name= 'reporte_Heroe_view'),
    path('reporte_Boxeador/', reporte_Boxeador, name= 'reporte_Boxeador_view'),
    path('reporte_Persona/', reporte_Persona, name= 'reporte_Persona_view'),
    path('reporte_DragonBall/', reporte_DragonBall, name= 'reporte_DragonBall_view'),

]
