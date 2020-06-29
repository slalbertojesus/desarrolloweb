from django.shortcuts import render
from django.shortcuts import redirect
from .models import Actividad
from .models import EstadoActividad
from accounts.models import Account 
from .forms import ActividadForm
from datetime import date

# Create your views here.
def MostrarActividades(request):
    actividades = Actividad.objects.filter(account = request.user)
    for actividad in actividades:
        if actividad.fechaEntrega < date.today():
            if actividad.estado.estado == "Sin realizar":
                print(actividad.estado)
                actividad.estado= EstadoActividad.objects.get(id=2)
                actividad.save()
        
    return render(request, "FeedActividades.html", {"actividades":actividades})



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
            
            
            return redirect('FeedActividades')
        else:
            form = ActividadForm()
            
        return render(request, 'crear_Actividad.html',{'form':form})

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
        return redirect('FeedActividades')
    return render(request,'editar_Actividad.html', {'form': form})

def eliminarActividad (request, id):
    actividad = Actividad.objects.get(id = id)
    if request.method == 'POST':
        actividad.delete()
        return redirect('FeedActividades')
    return render(request,'eliminar_actividad.html', {'aactividad':actividad})
    
def realizarActividad (request, id):   
    
    actividad = Actividad.objects.get(id = id)
    print("ks")
    if request.method == 'POST':
        print(actividad.fechaEntrega)
        if actividad.fechaEntrega < date.today():
            actividad.estado = EstadoActividad.objects.get(id=3)
            actividad.save()
            return redirect('FeedActividades')
        if actividad.fechaEntrega > date.today():
            actividad.estado = EstadoActividad.objects.get(id=4)
            actividad.save()
            return redirect('FeedActividades')
    return render(request, "actividadEstado.html", {"actividad":actividad})