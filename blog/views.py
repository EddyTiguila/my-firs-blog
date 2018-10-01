
from .models import Publicacion
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# Create your views here.

def listado (request):
    publicados = Publicacion.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render (request, 'blog/listar.html',{'publicados':publicados})
def detalle (request, pk):
     pub = get_object_or_404(Publicacion, pk=pk)
     return render(request, 'blog/detalle.html', {'pub': pub})
