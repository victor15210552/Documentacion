from django import forms
from Aplicacion.models import Ninja,Capitan,Equipo,ExamenChunin,Persona,Heroe,Boxeador,DragonBall
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

class Persona_form(forms.ModelForm):
	class Meta:
		model=Persona
		fields='__all__'

class Heroe_form(forms.ModelForm):
	class Meta:
		model=Heroe
		fields='__all__'

class Boxeador_form(forms.ModelForm):
	class Meta:
		model=Boxeador
		fields='__all__'

class DragonBall_form(forms.ModelForm):
	class Meta:
		model=DragonBall
		fields='__all__'

class Ninja_form(forms.ModelForm):
	class Meta:
		model=Ninja
		fields='__all__'

class Capitan_form(forms.ModelForm):
	class Meta:
		model=Capitan
		fields='__all__'

class Equipo_form(forms.ModelForm):
	class Meta:
		model=Equipo
		fields='__all__'

class ExamenChunin_form(forms.ModelForm):
	class Meta:
		model=ExamenChunin
		fields='__all__'