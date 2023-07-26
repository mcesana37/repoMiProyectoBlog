from django.contrib import admin
from .models import Categoria, Articulo, Comment

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Comment)
