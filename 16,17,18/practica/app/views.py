from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
#Prueva view dinamic
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import FormView
from app.forms import Persona_form,Ninja_form,Capitan_form,ExamenChunin_form,Heroe_form,Boxeador_form,DragonBall_form,Equipo_form
from app.models import Persona,Heroe,Boxeador,Ninja,DragonBall,Capitan,Equipo,ExamenChunin
# Create your views here.
def Persona(request):
     form=Persona_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Persona_form()
     return render(request,'Persona.html',{'form':form,'titulo':'Persona'})

def Heroe(request):
     form=Heroe_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Heroe_form()
     return render(request,'Heroe.html',{'form':form,'titulo':'Heroe'})

def Boxeador(request):
     form=Boxeador_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Boxeador_form()
     return render(request,'Boxeador.html',{'form':form,'titulo':'Boxeador'})

def DragonBall(request):
     form=DragonBall_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = DragonBall_form()
     return render(request,'DragonBall.html',{'form':form,'titulo':'DragonBall'})


def Capitan(request):
     form=Capitan_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Capitan_form()
     return render(request,'Capitan.html',{'form':form,'titulo':'Capitan'})


def Ninja(request):
     form=Ninja_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Ninja_form()
     return render(request,'Ninja.html',{'form':form,'titulo':'Ninja'})


def Equipo(request):
     form=Equipo_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Equipo_form()
     return render(request,'Equipo.html',{'form':form,'titulo':'Equipo'})

def ExamenChunin(request):
     form=ExamenChunin_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = ExamenChunin_form()
     return render(request,'ExamenChunin.html',{'form':form,'titulo':'ExamenChunin'})
#Gracias a que se importan los modelos no se pueden ejecutar los formularios 

#Crear ĺa vista del reporte
def reporte_Ninja(request):
  return render(request, 'reporte_Ninja.html', {'ninjas': Ninja.objects.all()})  

def reporte_Persona(request):
  return render(request, 'reporte_Persona.html', {'persona': Persona.objects.all()}) 

def reporte_Heroe(request):
  return render(request, 'reporte_Heroe.html', {'heroe': Persona.objects.all()}) 

def reporte_DragonBall(request):
  return render(request, 'reporte_DragonBall.html', {'dragonball': DragonBall.objects.all()}) 

def reporte_Boxeador(request):
  return render(request, 'reporte_Boxeador.html', {'boxeador': Boxeador.objects.all()}) 





