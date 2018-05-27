from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Autor(models.Model):
	nombre = models.CharField(max_length=100, primary_key=True)
	apellido = models.CharField(max_length=100)
	correo = models.CharField(max_length=100)

	def __str__(self):
		return  self.nombre + " " + self.apellido

class editorial(models.Model):
	nombre = models.CharField(max_length=150, primary_key=True)
	ubicacion = models.CharField(max_length=150)	

	def __str__(self):
			return self.nombre

class libro(models.Model):
	isbn = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre
	
class detalle_libro(models.Model):
	libro = models.ForeignKey( 'Libro', on_delete=models.CASCADE,)
	edicion = models.IntegerField()
	num_paginas = models.IntegerField()
	editorial = models.ForeignKey( 'editorial', on_delete=models.CASCADE,)
	autor = models.ForeignKey( 'Autor', on_delete=models.CASCADE,)

	def __str__(self):
			return self.libro.nombre 

class disponibilidad_libro(models.Model):
	tienda = models.CharField(max_length=120)
	nombre = models.ForeignKey( 'Libro', on_delete=models.CASCADE,)
	cantidad = models.IntegerField()
	slug = models.SlugField(unique = True)

	def __str__(self):
		return self.tienda

class modelo_extendido(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	apodo = models.CharField(max_length=120)
	facebook = models.CharField(max_length=120)
	youtube = models.CharField(max_length=120)
	equipo_favorito = models.CharField(max_length=120)

	def __str__(self):
		return self.user.username