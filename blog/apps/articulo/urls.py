from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articulo'

urlpatterns = [
    path('', views.ListarArticulos, name='listar'),
    path('listarArticulo/', views.mostrarArticulo.as_view()), #clase
    path('detalle/<int:pk>', views.DetalleArticulo, name='detalle'),
    path('addArticulo', views.AddArticulo, name='addArticulo'),
    path('articulo/<int:pk>/edit/', views.EditarArticulo, name='editarArticulo'),
    #url comentarios
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/add/<int:articulo_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
