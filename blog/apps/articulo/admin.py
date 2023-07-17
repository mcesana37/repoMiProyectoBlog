from django.contrib import admin
from .models import Categoria, Articulo

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Categoria)