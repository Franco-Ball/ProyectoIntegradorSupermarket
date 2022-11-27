from django import forms
from django.forms import ModelForm

from .models import Articulos,Turnos

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

class ArticulosForm2(ModelForm):
    class Meta:
        model = Articulos
        fields = ('codigo', 'stock', 'nombre', 'descripcion', 'precio')
        labels={
            'codigo': 'Código',
             'stock': 'Stock',
              'nombre': 'Nombre',
               'descripcion': 'Descripcion',
                'precio': 'Precio',
                }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Código'}),
             'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Stock'}),
              'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}),
               'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Descripcion'}),
                'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Precio',}),
                 
        }

class TurnosForm(ModelForm):
    class Meta:
        model = Turnos
        exclude = ('horaInicio', 'horaFin','turno_activo')
        #fields = ('detalle', 'horaInicio', 'horaFin', 'turno_activo', 'cajero')
        """ widgets = {
            'detalle': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Código'}),
            # 'horaInicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Stock'}),
              #'horaFin': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}),
                #'cajero': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'cajero',}),
                 
        }"""
