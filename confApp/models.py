from django.db import models

class Turnos(models.Models):
    detalle = models.CharField(max_length=30)
    horaInicio = models.IntegerField()
    horaFin = models.IntegerField()

class Direcciones(models.Models):
    calle = models.CharField(30)
    altura = models.IntegerField()
    barrio = models.CharField(30)
    provincia = models.CharField(30)

class Articulos(models.Models):
    codigo = models.IntegerField()
    stock = models.IntegerField()
    nombre = models.CharField(30)
    descripcion = models.CharField(30)
    precio = models.IntegerField()

class Ventas(models.Models):
    fecha = models.DateField()
    listaDetalleVenta = models.() ###
	
class detalleVentas(models.Models):
    numVenta = models.IntegerField()
    numArticulo = models.IntegerField()
    precioUnidad = models.IntegerField()
    cantidad = models.IntegerField()
	
class Asignaciones(models.Models):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    listaDeVenta = models.() ###
	
class Cajas(models.Models):
    estado = models.BooleanField()
    listaDeAsignacion = models.() ###

class Sucursal(models.Models):
    telefono = models.CharField(30)
    direccion = models.CharField(30)
    listaDeCaja = models.() ###

class Cajero(models.Models):
    dni = models.CharField(30)
    nombre = models.CharField(30)
    apellido = models.CharField(30)
    nacimiento = models.DateField()
    direccion = models.() ###
    telefono = models.CharField(30)
    ingresoEmpresa = models.DateField()
    email = models.CharField(50)
    listaAsignacion = models.Asignacion()
    turnoTrabajo = models.() ###
    sucursal = models.() ###