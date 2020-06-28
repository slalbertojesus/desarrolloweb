from django.contrib import admin
from .models import Actividad
from .models import EstadoActividad

# Register your models here.
admin.site.register(Actividad)
admin.site.register(EstadoActividad)
