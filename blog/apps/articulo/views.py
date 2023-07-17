from django.shortcuts import render
from .models import Articulo
from django.views.generic.list import ListView #para las vistas clases

# Create your views here.
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