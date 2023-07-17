from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articulo'

urlpatterns = [
    path('', views.ListarArticulos, name='listar'),
    path('listarArticulo/', views.mostrarArticulo.as_view()), #clase
    path('detalle/<int:pk>', views.DetalleArticulo, name='detalle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


