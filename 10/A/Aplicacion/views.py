from django.shortcuts import render

# Create your views here.
def vista1A(request):
    return render(request, 'vista1.html')
def vista2(request):
    return render(request, 'vista2.html')
def vista3(request):
    return render(request, 'vista3.html')
def vista4(request):
    return render(request, 'vista4.html')
def vista5(request):
    return render(request, 'vista5.html')

from Aplicacion.forms import Persona_form,Ninja_form,Capitan_form,ExamenChunin_form,Heroe_form,Boxeador_form,DragonBall_form,Equipo_form

# Create your views here.
def Persona(request):
     form=Persona_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Persona_form()
     return render(request,'Persona.html',{'form':form,'titulo':'Persona'})

#def Heroe(request):
 #    form=Heroe_form(request.POST or None)
  #   if request.method=='POST':
   #  	if form.is_valid():
    ## 		form.save()
     #		form = Heroe_form()
    # return render(request,'Heroe.html',{'form':form,'titulo':'Heroe'})

def Heroe(request):
	form=Heroe_form()
	return render(request, 'Heroe.html',{'form':form})

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

def Ninja(request):
     form=Ninja_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Ninja_form()
     return render(request,'Ninja.html',{'form':form,'titulo':'Ninja'})

def Capitan(request):
     form=Capitan_form(request.POST or None)
     if request.method=='POST':
     	if form.is_valid():
     		form.save()
     		form = Capitan_form()
     return render(request,'Capitan.html',{'form':form,'titulo':'Capitan'})

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


#GENERAR REPORTE
#1. importar el modelo
from Aplicacion.models import Persona,Heroe,Boxeador,Ninja,DragonBall,Capitan,Equipo,ExamenChunin

#2. Crear ĺa vista del reporte
def reporte_Ninja(request):
  return render(request, 'reporte_Ninja.html', {'ninjas': Ninja.objects.all()})  






























