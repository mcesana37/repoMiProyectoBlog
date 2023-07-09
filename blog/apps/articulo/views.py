from django.shortcuts import render

# Create your views here.
def ListarArticulos(request):
    return render(request, 'articulo/listar.html')