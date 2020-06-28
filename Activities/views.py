from django.shortcuts import render
from .models import Actividad
from .models import EstadoActividad
from accounts.models import Account 

# Create your views here.
def MostrarActividades(request):
    actividades = Actividad.objects.all()
    return render(request, "FeedActividades.html", {"actividades":actividades})