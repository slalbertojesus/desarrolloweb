from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.utils import timezone
from Activities.models import *
from .render import Render


class Pdf(View):

    @method_decorator(login_required)
    def get(self, request):
        actividades = Actividad.objects.filter(account = request.user)
        
        params = {
            
            'actividades': actividades,
            'request': request
        }
        return Render.render('pdf.html', params)