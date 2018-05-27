from django.forms import ModelForm

#importar
from django import forms
from django.contrib.auth.forms import UserCreationForm

class form_registro(UserCreationForm):
	apodo  = forms.CharField(max_length= 120)
	facebook = forms.CharField(max_length= 120)
	youtube = forms.CharField(max_length= 120)
	equipo_favorito = forms.CharField(max_length= 120)
	