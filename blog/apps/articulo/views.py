from django.shortcuts import render, redirect
from .models import Articulo, Categoria, Comentario, Usuario
from django.views.generic.list import ListView #para las vistas clases
from .forms import ArticuloForm, ComentarioForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def AddArticulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.author = request.user #autor del articulo            noticia.save()
            return redirect('home')
    else:
        form = ArticuloForm()
    
    return render(request, 'articulo/addArticulo.html', {'form': form})


def ListarArticulos(request):
    contexto = {} #DICCIONARIO

    n = Articulo.objects.all() #SELECT ALL

    contexto['articulo'] = n

    return render(request, 'articulo/listar.html', contexto)

#VISTA CON CLASES
class mostrarArticulo(ListView):
    model = Articulo
    template_name = 'articulo/listarArticulo.html'

def DetalleArticulo(request, pk):
    contexto = {} #diccionario

    n = Articulo.objects.get(pk = pk) # 1 solo objeto

    contexto['articulo'] = n

    return render(request, 'articulo/detalle.html', contexto)