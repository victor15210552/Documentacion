from django.forms import ModelForm

#importar
from django import forms
from django.contrib.auth.forms import UserCreationForm

class form_registro(UserCreationForm):
	apodo  = forms.CharField(max_length= 120)
	salario = forms.IntegerField()
	correo_electronico = forms.CharField(max_length=120)
	nivel_educativo = forms.CharField(max_length=30)