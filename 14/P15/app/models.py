# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Alumno(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	correo = models.CharField(max_length=50)

	def __str__(self):
		return  self.nombre

class Mestro(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	correo = models.CharField(max_length=50)

	def __str__(self):
			return self.nombre

class Clase(models.Model):
	nombre = models.CharField(max_length=30)
	creditos = models.IntegerField()

	def __str__(self):
			return self.nombre + " " + str(self.creditos)
	
class Horario(models.Model):
	turno = models.CharField(max_length=100)
	hora = models.CharField(max_length=100)

	def __str__(self):
			return self.turno + " " + self.hora

class Carrera(models.Model):
	nombre = models.CharField(max_length=30)
	creditos = models.IntegerField()

	def __str__(self):
		return self.nombre + ", creditos " + str(self.creditos)

from django.db import models
from django.contrib.auth.models import User


class modelo_Extendido(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	salario = models.IntegerField()
	correo_electronico = models.CharField(max_length=120)
	nivel_educativo = models.CharField(max_length=30)

	def __str__(self):
		return self.user.username