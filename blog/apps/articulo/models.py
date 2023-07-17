from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length= 100)
    
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

    def __str__(self):
        return self.titulo