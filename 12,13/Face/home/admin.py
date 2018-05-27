from django.contrib import admin
from .models import Perfil, Comment, Publication
# Register your models here.
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
	list_display = ['user_perfil', 'email', 'get_friends']

@admin.register(Comment)
class PerfilAdmin(admin.ModelAdmin):
	list_display = ['comment', 'score', 'user', 'publication']

@admin.register(Publication)
class PerfilAdmin(admin.ModelAdmin):
	list_display = ['title', 'body', 'score','user', 'unscored']