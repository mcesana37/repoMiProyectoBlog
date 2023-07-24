from django import forms
from .models import Articulo, Comentario

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria_articulo']

# CREAR COMENTARIOS
class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['text'] #campos de mi formulario
       
   