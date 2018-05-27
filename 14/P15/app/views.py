# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

from app import models
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

class formulario_Alumno(CreateView):
    template_name= "app/formulario_Alumno.html"
    model = models.Alumno
    fields = "__all__"
    success_url = reverse_lazy("formulario_Alumno")

class formulario_Mestro(CreateView):
    template_name= "app/formulario_Mestro.html"
    model = models.Mestro
    fields = "__all__"
    success_url = reverse_lazy("formulario_Mestro")

class formulario_Clase(CreateView):
    template_name= "app/formulario_Clase.html"
    model = models.Clase
    fields = "__all__"
    success_url = reverse_lazy("formulario_Clase")

class formulario_Horario(CreateView):
    template_name= "app/formulario_Horario.html"
    model = models.Horario
    fields = "__all__"
    success_url = reverse_lazy("formulario_Horario")

class formularo_Carrera(CreateView):
    template_name= "app/formularo_Carrera.html"
    model = models.Carrera
    fields = "__all__"
    success_url = reverse_lazy("formularo_Carrera")
