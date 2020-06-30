from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.utils import timezone
from Activities.models import *
from .render import Render


class Pdf(View):

    def get(self, request):
        actividades = Actividad.objects.all()
        
        params = {
            
            'actividades': actividades,
            'request': request
        }
        return Render.render('pdf.html', params)