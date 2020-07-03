"""proyectoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, pathzx123321xz

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Activities.views import MostrarActividades
from Activities.views import crearActividad
from Activities.views import editarActividad
from Activities.views import eliminarActividad
from Activities.views import realizarActividad
from Report.views import Pdf
from ReportAdmin.views import Report




urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('FeedActividades/<str:campo>', MostrarActividades, name = "FeedActividades"),
    path ('crear_Actividad/', crearActividad, name = "crear_Actividad"),
    path ('editar_Actividad/<int:id>', editarActividad, name = "editar_Actividad"),
    path ('eliminar_Actividad/<int:id>', eliminarActividad, name = "eliminar_Actividad"),
    path ('actividadEstado/<int:id>', realizarActividad, name = "actividadEstado"),
    path('render/pdf/', Pdf.as_view(),name = "render/pdf"),
    path('render/pdfAdmin/', Report.as_view(),name = "render/pdfAdmin"),

]
