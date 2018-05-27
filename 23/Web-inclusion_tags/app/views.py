from django.shortcuts import render

def view_base(request):
	return render(request, 'app/base.html')

#6 DE MARZO SERVIR JSON 
from django.http import HttpResponse
from django.core import serializers
from  app import models
import json

#para servir usa los archivos views.py y urls.py

def json_autor(request):
    data = serializers.serialize('json', models.Autor.objects.all())
    return HttpResponse(data, "application/json")

def json_editorial(request):
    data = serializers.serialize('json', models.editorial.objects.all())
    return HttpResponse(data, "application/json")

def json_libro(request):
    data = serializers.serialize('json', models.libro.objects.all())
    return HttpResponse(data, "application/json")

def json_detalle_libro(request):
    data = serializers.serialize('json', models.detalle_libro.objects.all())
    return HttpResponse(data, "application/json")

def json_disponibilidad_libro(request):
    data = serializers.serialize('json', models.disponibilidad_libro.objects.all())
    return HttpResponse(data, "application/json")

def json_modelo_extendido(request):
    data = serializers.serialize('json', models.modelo_extendido.objects.all())
    return HttpResponse(data, "application/json")


# 6 DE MARZO CONSUMIR JSON.
def consumir_autor(request):
   return render(request, 'app/consum_json_autor.html')

def consumir_detalle(request):
   return render(request, 'app/consum_json_detalle.html')

def consumir_disponibilidad(request):
   return render(request, 'app/consum_json_disponibilidad.html')

def consumir_editorial(request):
   return render(request, 'app/consum_json_editorial.html')

def consumir_libro(request):
   return render(request, 'app/consum_json_libro.html')

def consumir_extendido(request):
   return render(request, 'app/consum_json_extendido.html')
