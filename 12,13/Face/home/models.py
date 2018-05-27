from __future__ import unicode_literals
from django.db import models
##from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Perfil(models.Model):
	user_perfil = models.OneToOneField(User,on_delete=models.CASCADE)
	email = models.EmailField()
	image = models.ImageField(upload_to='perfil_FaceRay/', blank=True, null=True, default='../static/user.png')
	friends = models.ManyToManyField("self", blank=True)

	#Metodo para devolder
	def __unicode__(self):
		return self.user_perfil.username

	def get_friends(self):
		return "\n , ".join([str(p.user_perfil) for p in self.friends.all()])

class Publication(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	score = models.PositiveIntegerField(blank=True, null=True, default=0)
	unscored = models.PositiveIntegerField(blank=True, null=True, default=0)
	user = models.CharField(max_length=50)

	def __unicode__(self):
		return unicode(self.title)

class Comment(models.Model):
	comment = models.TextField()
	score = models.PositiveIntegerField(blank=True, null=True, default=0)
	user = models.CharField(max_length=50)
	publication = models.ForeignKey("Publication",on_delete=models.CASCADE)

	def __unicode__(self):
		return unicode(self.comment)
