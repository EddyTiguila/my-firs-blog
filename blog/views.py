from django.shortcuts import render
from .models import Publicacion
from django.utils import timezone
# Create your views here.

def listado (request):
    publicados = Publicacion.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render (request, 'blog/listar.html',{'publicados':publicados})
