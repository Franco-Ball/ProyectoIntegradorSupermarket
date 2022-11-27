from django.shortcuts import render
from .models import *
from .forms import ArticulosForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_screen_view(request):
    articulos = Articulos.objects.all
    return render(request, "principal.html", {'articulo':articulos})

def signin_screen_view(request):
    return render(request, "signin.html")

def cambio_DB(request):
    submitted = False
    if request.method == "POST":
        form = ArticulosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/changeDB?submitted=True')
    else:
        form = ArticulosForm
    return render(request, "changeDB.html", {'form':form, 'submitted':submitted})

def cajeros_view(request):
    return render(request, "cajeros/base.html")