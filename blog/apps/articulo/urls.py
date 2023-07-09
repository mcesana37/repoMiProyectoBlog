from django.urls import path
from . import views 

app_name = 'articulo'

urlpatterns = [
    path('', views.ListarArticulos, name='listar'),
]
