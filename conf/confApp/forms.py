from django import forms
from django.forms import ModelForm

from .models import Articulos

class ArticulosForm(ModelForm):
    class Meta:
        model = Articulos
        fields = ('codigo', 'stock', 'nombre', 'descripcion', 'precio', 'imagen')