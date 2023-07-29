from django.db import models
from apps.usuarios.models import Usuario
from django.conf import settings 

class Categoria(models.Model):
    nombre = models.CharField(max_length= 200)
        
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
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE) # default=Usuario.objects.get(is_superuser=True).pk)

    def __str__(self):
        return self.titulo
    
class Comment(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
