from django.shortcuts import render
from django.shortcuts import redirect
from .models import Actividad
from .models import EstadoActividad
from accounts.models import Account 
from .forms import ActividadForm

# Create your views here.
def MostrarActividades(request):
    actividades = Actividad.objects.all()
    return render(request, "FeedActividades.html", {"actividades":actividades})

def crearActividad(request):
    if request.method == 'GET':
        form = ActividadForm()
        return render(request, 'crear_Actividad.html',{'form':form})
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            
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
    