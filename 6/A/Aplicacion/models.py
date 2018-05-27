from django.db import models

# Create your models here.
class Persona(models.Model):
	first_name=models.CharField(max_length=30) 
	last_name=models.CharField(max_length=30)
	birthday=models.DateTimeField()
	born_city=models.CharField(max_length=30)
	sex=models.CharField(max_length=30)
	blood=models.CharField(max_length=30)
	status=models.CharField(max_length=30,default='None' )
	job=models.CharField(max_length=30,default='None')
	year=models.CharField(max_length=30, default='None')
	def __str__(self):
		return (self.first_name,self.last_name)


class Heroe (models.Model):
	nombre=models.CharField(max_length=30)
	superpower=models.CharField(max_length=30)
	color_piel=models.CharField(max_length=30)
	Estatus=models.CharField(max_length=30)
	edad=models.CharField(max_length=30)
	edad=models.CharField(max_length=30)
	nacionalidad=models.CharField(max_length=30)
	color=models.CharField(max_length=30)
	sexo=models.CharField(max_length=30)
	Clase=models.CharField(max_length=30)
	def __str__(self):
		return "Name: %s, Poder: %s"%(self.nombre, self.superpower)


class Boxeador (models.Model):
	nombre=models.CharField(max_length=30)
	Ganadas=models.FloatField(max_length=30)
	Natalidad=models.CharField(max_length=30)
	Perdidas=models.CharField(max_length=30)
	Empates=models.CharField(max_length=30)
	edad=models.CharField(max_length=30)
	nacionalidad=models.CharField(max_length=30)
	Peso = models.FloatField()
	Categoria = models.CharField(max_length=30)
	AtaqueEspecial=models.CharField(max_length=30)
	def __str__(self):
		return "Name: %s"%(self.nombre)

class Ninja (models.Model):
	nombre=models.CharField(max_length=30)
	level_chakra=models.FloatField()
	LugardeOrigen=models.CharField(max_length=30)
	Naturaleza=models.CharField(max_length=30)
	clan=models.CharField(max_length=24)
	edad=models.CharField(max_length=30)
	militar_range=models.CharField(max_length=24)
	Armas = models.FloatField()
	elite=models.BooleanField(default=False)
	AtaqueEspecial=models.CharField(max_length=30)
	def __str__(self):
		return "Name: %s, Natulareza: %s"%(self.nombre, self.Naturaleza)

class DragonBall (models.Model):
	nombre=models.CharField(max_length=30)
	Categoria=models.CharField(max_length=30,default="Ninguna")
	LugardeOrigen=models.CharField(max_length=30)
	Fases_evolucion=models.CharField(max_length=30)
	kii=models.FloatField()
	edad=models.FloatField()
	color_piel=models.CharField(max_length=30)	
	Punto_debil= models.CharField(max_length=30)
	AtaqueEspecial=models.CharField(max_length=30)
	def __str__(self):
		return "Name: %s"%(self.nombre)


class Capitan(models.Model):
	nombre=models.CharField(max_length=30)
	niveldechakra=models.FloatField()
	Rango=models.CharField(max_length=30)
	LugardeOrigen=models.CharField(max_length=30)
	Naturaleza=models.CharField(max_length=30)
	Clan=models.CharField(max_length=30)
	edad=models.CharField(max_length=30)
	def __str__(self):
		return "Name: %s, Naturaleza: %s"%(self.nombre, self.Naturaleza)

class Equipo(models.Model):
	Capitan=models.ForeignKey(Capitan, on_delete=models.CASCADE)
	Genins=models.ManyToManyField(Ninja)
	slug=models.SlugField(max_length=30,unique=True)
	Nombre_Equipo= models.CharField(max_length=30)
	def __str__(self):
		return "Number Team: %s"%(self.Nombre_Equipo)

class ExamenChunin(models.Model):
	Equipos=models.ManyToManyField(Equipo)
	NumeroEquipo=models.FloatField()
	slug=models.SlugField(max_length=30,unique=True)
	def __str__(self):
		return "Name: %s"%(self.NumeroEquipo)
