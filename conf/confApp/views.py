from django.shortcuts import render
from .models import *

# Create your views here.
def home_screen_view(request):
    articulos = Articulos.objects.all
    return render(request, "principal.html", {'articulo':articulos})

def signin_screen_view(request):
    return render(request, "signin.html")

def cajeros_view(request):
    return render(request, "cajeros/base.html")