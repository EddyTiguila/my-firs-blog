
from .models import Publicacion
from django.utils import timezone
from .forms import NuevoForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def listado (request):
    publicados = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_creacion')
    return render (request, 'blog/listar.html',{'publicados':publicados})
def detalle (request, pk):
     pub = get_object_or_404(Publicacion, pk=pk)
     return render(request, 'blog/detalle.html', {'pub': pub})
def post_publish(request, pk):
         post = get_object_or_404(Publicacion, pk=pk)
         post.publicar()
         return redirect('detalle', pk=pk)
def post_remove(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.delete()
    return redirect('listado')

def nuevoPost(request):
        if request.method == "POST":
            form = NuevoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('listado')
        else:
            form = NuevoForm()
        return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
        post = get_object_or_404(Publicacion, pk=pk)
        if request.method == "POST":
            form = NuevoForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('listado')
        else:
            form = NuevoForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
def post_draft_list(request):
    post = Publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/post_draft_list.html', {'post': post})
