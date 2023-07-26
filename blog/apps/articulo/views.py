from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, Categoria, Comment, Usuario
from django.views.generic.list import ListView #para las vistas clases
from .forms import ArticuloForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden



# Create your views here.
@login_required
def AddArticulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.author = request.user #autor del articulo            
            return redirect('home')
    else:
        form = ArticuloForm()
    
    return render(request, 'articulo/addArticulo.html', {'form': form})


def ListarArticulos(request):
    articulo = Articulo.objects.all()

    #FILTRAR POR ANTIGÜEDAD DESDE EL MÁS RECIENTE (DESCENDENTE)
    antiguedad_desc = request.GET.get('antiguedad_desc')
    if antiguedad_desc:
        articulo = articulo.order_by('-fecha_publicacion')

    #FILTRAR POR ANTIGÜEDAD DESDE EL MÁS ANTIGUO (ASCENDENTE)
    antiguedad_asc = request.GET.get('antiguedad_asc')
    if antiguedad_asc:
        articulo = articulo.order_by('fecha_publicacion')

     # Filtrar por orden alfabético ascendente
    orden_asc = request.GET.get('orden_asc')
    if orden_asc:
        articulo = articulo.order_by('titulo')

    # Filtrar por orden alfabético descendente
    orden_desc = request.GET.get('orden_desc')
    if orden_desc:
        articulo = articulo.order_by('-titulo')

     # Filtrar por categoría
    categoria = request.GET.get('categoria')
    if categoria:
        articulo = articulo.filter(categoria_articulo=categoria)

    context = {
        'articulo': articulo,
        'categoria': Categoria.objects.all(),  
    }
    return render(request, 'articulo/listar.html', context)  
   

#VISTA CON CLASES
class mostrarArticulo(ListView):
    model = Articulo
    template_name = 'articulo/listarArticulo.html'

def DetalleArticulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    comments = articulo.comments.all() 
    
    #BORRAR ARTICULO
    if request.method == 'POST' and 'delete_articulo' in request.POST:
        articulo.delete()
        return redirect('articulo:listar')

 # COMENTARIO
    if request.method == 'POST' and 'add_comment' in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.articulo = articulo
            comment.author = request.user
            comment.save()
            return redirect('articulo:detalle', pk=pk)
    else:
        form = CommentForm()

    context = {
        'articulo': articulo,
        'comments': comments,
        'form': form,
    }
    return render(request, 'articulo/detalle.html', context)

@login_required
def add_comment(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.user.username
        # creacion de comentario
        Comment.objects.create(articulo=articulo, author=author, text=text)
    return redirect('articulo:detalle', pk=articulo_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author or comment.staff == request.user.username:
        comment.delete()
    return redirect('articulo:detalle', pk=comment.articulo.pk)

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    #mensaje de error si no sos el autor
    if comment.author != request.user.username:
        messages.error(request, 'Usuario sin permisos para editar este comentario.')
        return redirect('articulo:detalle', pk=comment.articulo.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('articulo:detalle', pk=comment.articulo.pk)
    else:
        form = CommentForm(instance=comment)

    context = {
        'form': form,
        'comentario': comment,
    }
    return render(request, 'articulo/editComentario.html', context)

@login_required
def EditarArticulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)

    # Solo el autor puede editar la noticia
    if articulo.author != request.user:
        return HttpResponseForbidden("No tienes permisos para editar este artículo.")

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulo:detalle', pk=pk)
    else:
        form = ArticuloForm(instance=articulo)

    context = {
        'form': form,
        'articulo': articulo,
    }
    return render(request, 'articulo/editArticulo.html', context)