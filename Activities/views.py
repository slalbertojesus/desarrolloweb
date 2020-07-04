from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Actividad
from .models import EstadoActividad
from accounts.models import Account 
from .forms import ActividadForm
from datetime import date
from datetime import datetime

# Create your views here.
@login_required
def MostrarActividades(request, campo):
    actividades = Actividad.objects.filter(account = request.user).order_by(campo)
    for actividad in actividades:
        if actividad.fechaEntrega < date.today():
            if actividad.estado.estado == "Sin realizar":
                
                actividad.estado= EstadoActividad.objects.get(id=2)
                actividad.save()
        
            
    return render(request, "FeedActividades.html", {"actividades":actividades})



@login_required
def crearActividad(request):
    if request.method == 'GET':
        form = ActividadForm()
        return render(request, 'crear_Actividad.html',{'form':form})
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit = False)
            actividad.account = request.user
            actividad.estado = EstadoActividad.objects.get(id = 1)
            actividad.save()
            return redirect('FeedActividades', campo="nombre")
        else:
            return render(request, 'crear_Actividad.html',{'form':form})    
        
    
        return render(request, 'crear_Actividad.html',{'form':form})

@login_required
def editarActividad(request, id):
    if request.method == 'GET':
        form = ActividadForm()
    actividad = Actividad.objects.get(id = id)
    if request.method == 'GET':
        form = ActividadForm(instance = actividad)
    else:
        form = ActividadForm(request.POST, instance = actividad)
        if form.is_valid():
            form.save()
            return redirect('FeedActividades', campo="nombre")
        else:
            return render(request, 'editar_Actividad.html',{'form':form}) 
    return render(request, 'editar_Actividad.html',{'form':form}) 

@login_required
def eliminarActividad (request, id):
    actividad = Actividad.objects.get(id = id)
    if request.method == 'POST':
        actividad.delete()
        return redirect('FeedActividades', campo="nombre")
    return render(request,'eliminar_actividad.html', {'actividad':actividad})
    
@login_required
def realizarActividad (request, id):   
    
    actividad = Actividad.objects.get(id = id)
   
    if request.method == 'POST':
        actividad.fechaRealizacion= date.today()
        if actividad.fechaEntrega <= date.today():
            actividad.estado = EstadoActividad.objects.get(id=3)
            actividad.save()
            return redirect('FeedActividades', campo="nombre")
        if actividad.fechaEntrega > date.today():
            actividad.estado = EstadoActividad.objects.get(id=4)
            actividad.save()
            return redirect('FeedActividades', campo="nombre")
    return render(request, "actividadEstado.html", {"actividad":actividad})