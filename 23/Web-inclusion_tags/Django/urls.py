"""Django URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.view_base),

	#6 MARZO Servir Json
    path("json_autor/", views.json_autor),
    path("json_editorial/", views.json_editorial),
    path("json_libro/", views.json_libro),
    path("json_detalle_libro/", views.json_detalle_libro),
    path("json_disponibilidad_libro/", views.json_disponibilidad_libro),
    path("json_modelo_extendido/", views.json_modelo_extendido),

	#6 MARZO Consumir Json
    path("consumir_autor/", views.consumir_autor),
    path("consumir_detalle/", views.consumir_detalle),
    path("consumir_disponibilidad/", views.consumir_disponibilidad),
    path("consumir_editorial/", views.consumir_editorial),
    path("consumir_libro/", views.consumir_libro),
    path("consumir_extendido/", views.consumir_extendido),
]
