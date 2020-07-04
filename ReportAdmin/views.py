from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.utils import timezone
from Activities.models import *
from Report.render import Render
from datetime import date
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required


@login_required  
@staff_member_required
def MostrarActividadesAdmin(request, campo):
    actividades = Actividad.objects.order_by(campo)
    for actividad in actividades:
        if actividad.fechaEntrega < date.today():
            if actividad.estado.estado == "Sin realizar":
                
                actividad.estado= EstadoActividad.objects.get(id=2)
                actividad.save()
        
            
    return render(request, "FeedActividadesAdmin.html", {"actividades":actividades})          


class Report(View):

    @method_decorator(login_required)
    @method_decorator(staff_member_required)
    def get(self, request):
        actividades = Actividad.objects.all()
        
        params = {
            
            'actividades': actividades,
            'request': request
        }
        return Render.render('pdfAdmin.html', params)

