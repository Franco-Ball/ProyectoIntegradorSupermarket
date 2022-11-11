from django.db import models

class Turnos(models.Models):
    detalle = models.CharField(max_length=30)
    horaInicio = models.IntegerField(max_length=2, default=8)
    horaFin = models.IntegerField(max_length=2, default=20)

class Direcciones(models.Models):
    calle = models.CharField(max_length=30, default="Calle")
    altura = models.IntegerField(max_length=5, default=12345)
    barrio = models.CharField(max_length=70, default="Barrio")
    provincia = models.CharField(max_length=30, default="Provincia")

class Articulos(models.Models):
    codigo = models.IntegerField(max_length=30, default=123456)
    stock = models.IntegerField(max_length=30, default=1)
    nombre = models.CharField(max_length=50, default="Articulo")
    descripcion = models.CharField(max_length=200, default="Descripcion")
    precio = models.IntegerField(max_length=30, default=100)
    
class detalleVentas(models.Models):
    numVenta = models.IntegerField(max_length=30, default=1234)
    numArticulo = models.IntegerField(max_length=30, default=1234)
    precioUnidad = models.IntegerField(max_length=30, default=1234)
    cantidad = models.IntegerField(max_length=30, default=1234)

class Ventas(models.Models):
    fecha = models.DateField(default= "2022-09-06")
    listaDetalleVenta = models.ForeignKey(
        detalleVentas,
        on_delete=models.CASCADE, default=1
    )
	
class Asignaciones(models.Models):
    fechaInicio = models.DateField(default= "2022-09-06")
    fechaFin = models.DateField(default= "2022-09-06")
    listaDeVenta = models.ForeignKey(
        Ventas,
        on_delete=models.CASCADE, default=1
    )
	
class Cajas(models.Models):
    estado = models.BooleanField(default=True)
    listaDeAsignacion = models.ForeignKey(
        Asignaciones,
        on_delete=models.CASCADE, default=1
    )

class Sucursal(models.Models):
    telefono = models.CharField(max_length = 20, default="3513897259")
    direccion = models.CharField(max_length = 50, default="Direccion")
    listaDeCaja = models.ForeignKey(
        Cajas,
        on_delete=models.CASCADE, default=1
    )

class Cajero(models.Models):
    dni = models.CharField(max_length = 8, default="46037183")
    nombre = models.CharField(max_length = 30, default="Nombre")
    apellido = models.CharField(max_length = 30, default="Apellido")
    nacimiento = models.DateField(default= "2022-09-06")
    direccion = models.ForeignKey(
        Direcciones,
        on_delete=models.CASCADE, default=1
    )

    telefono = models.CharField(max_length = 20, default="3513897259")
    ingresoEmpresa = models.DateField(default= "2022-09-06")
    email = models.CharField(default="mailfalso@gmail.com")
    listaAsignacion = models.ForeignKey(
        Asignaciones,
        on_delete=models.CASCADE, default=1
    )
    turnoTrabajo = models.ForeignKey(
        Turnos,
        on_delete=models.CASCADE, default=1
    )
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE, default=1
    )