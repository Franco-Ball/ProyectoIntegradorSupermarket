from django import forms
from django.forms import ModelForm

from .models import Articulos

class ArticulosForm(ModelForm):
    class Meta:
        model = Articulos
        fields = ('codigo', 'stock', 'nombre', 'descripcion', 'precio', 'imagen')
        labels={
            'codigo': 'Código',
             'stock': 'Stock',
              'nombre': 'Nombre',
               'descripcion': 'Descripcion',
                'precio': 'Precio',
                 'imagen': 'Imagen'
                }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Código'}),
             'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Stock'}),
              'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}),
               'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Descripcion'}),
                'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Precio',}),
                 
        }