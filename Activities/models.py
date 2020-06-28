from django.db import models
from accounts.models import Account 

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion =models.TextField(max_length=250)
    estado = models.ForeignKey("EstadoActividad",blank=True, null=True, on_delete=models.CASCADE)
    fechaRealizacion = models.DateField(blank=True, null=True)
    fechaEntrega =  models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EstadoActividad(models.Model):

    
    estado =  models.CharField(max_length=50)

    def __str__(self):
        return self.estado

    
