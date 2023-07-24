from django.db import models
from apps.usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length= 200)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=2000)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    #instalar una librería pillow
    imagen = models.ImageField(upload_to= 'articulo')
    categoria_articulo = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    text = models.TextField(max_length= 1500)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
