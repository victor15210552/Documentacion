from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class User_form(UserCreationForm):
	email = forms.CharField(max_length=24)
	image = forms.ImageField(required = False)

