# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#importando los modelos de la app
from app import models
# Register your models here.
admin.site.register(models.Alumno)
admin.site.register(models.Mestro)
admin.site.register(models.Clase)
admin.site.register(models.Horario)
admin.site.register(models.Carrera)
admin.site.register(models.modelo_Extendido)