from django.shortcuts import render, redirect
from .models import *
from .forms import ArticulosForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_screen_view(request):
    articulos = Articulos.objects.all
    return render(request, "principal.html", {'articulo':articulos})

def home_screen_view2(request):
    articulos = Articulos.objects.all
    return render(request, "listArt.html", {'articulo':articulos})

def signin_screen_view(request):
    return render(request, "signin.html")

def cambio_DB(request):
    submitted = False
    if request.user.is_superuser:
        
        if request.method == "POST":
            form = ArticulosForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/changeDB?submitted=True')
        else:
            form = ArticulosForm()
        return render(request, "changeDB.html", {'form':form, 'submitted':submitted})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

def cajeros_view(request):
    if request.user.is_active:
        articulos = Articulos.objects.all
        return render(request, "cajeros/base.html", {'articulo':articulos})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

def art_update(request, articulo_id):
     if request.user.is_superuser:
        art = Articulos.objects.get(pk=articulo_id)
        form = ArticulosForm(request.POST, request.FILES or None, instance =art)
        if form.is_valid():
                form.save()
                return redirect('http://127.0.0.1:8000/accounts/login/')

        
        return render(request, "updateArt.html", {'art': art, 'form':form})
    
     else:
        return redirect('listado')
