from django.shortcuts import render, redirect
from .models import *
from .forms import ArticulosForm, ArticulosForm2, TurnosForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import datetime

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
        searched = None
        if request.method=="POST":
            turno_id = list(Turnos.objects.all().filter(cajero__usuario=request.user , turno_activo = True).values())[0]['id']
            turno = Turnos.objects.get(id = turno_id)
            searched = request.POST['searched']
            if searched:
                searched = Articulos.objects.filter(
                Q(nombre__icontains = searched) |
                Q(precio__icontains = searched)
                ).distinct()
        
        #search_result = Articulos.objects.filter(nombre__icontains=search)
            return render(request, "cajeros/base.html", {'articulo':articulos, 'searched':searched})
        else:
            form = TurnosForm()
            db = Turnos.objects.all()

        activo = len(list(Turnos.objects.all().filter(cajero__usuario=request.user , turno_activo = True).values())) > 0
        print(activo)
        #activo = True
        return render(request, 'cajeros/base.html', {'form': form, 'activo':activo})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')


def art_update(request, articulo_id):
     if request.user.is_superuser:
        art = Articulos.objects.get(pk=articulo_id)
        form = ArticulosForm2(request.POST or None, instance =art)
        if form.is_valid():
                form.save()
                return redirect('http://127.0.0.1:8000/listArt/')

        
        return render(request, "updateArt.html", {'art': art, 'form':form})
    
     else:
        return redirect('listado')

def cargar_turnos(request):
    if request.user.is_active:
    
        if request.method == 'POST':
            
            form = TurnosForm(request.POST)
            
            if form.is_valid():
                
                fk_cajero = Cajero.objects.all().filter(usuario=request.user)[0]
                turno = form.save(commit=False)
                turno.horaInicio = datetime.now()
                turno.turno_activo = True
                turno.horaFin = datetime.now()
                turno.operador = fk_cajero
                turno.save()

                return redirect('http://127.0.0.1:8000/cajeros/base/')
        else:
            form = TurnosForm()
        turnos_activos = Turnos.objects.all().filter(turno_activo=True, cajero__usuario = request.user)

        if len(turnos_activos) > 0:

            activar_form = False

        else:
            activar_form = True        
        return render(request, 'cajeros/turnos.html', {'form':form,
                                                        'activar_form':activar_form})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')