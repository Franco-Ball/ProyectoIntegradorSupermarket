from django.db import models
from django.conf import settings

class Direcciones(models.Model):
    calle = models.CharField(max_length=30, default="Calle")
    altura = models.IntegerField( default=12345)
    barrio = models.CharField(max_length=70, default="Barrio")
    provincia = models.CharField(max_length=30, default="Provincia")

    def __str__(self):
        return f"{self.calle}, {self.altura}"

class Sucursal(models.Model):
    telefono = models.CharField(max_length = 20, default="3513897259")
    direccion = models.ForeignKey(
        Direcciones,
        on_delete=models.CASCADE, default=1
    )
    def __str__(self):
        return f"{self.direccion}"        
    
class Cajas(models.Model):
    estado = models.BooleanField(default=True)
    listaDeSucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE, default=1
    )
    def __str__(self):
        return f"{self.estado}, {self.listaDeSucursal}"



class Cajero(models.Model):
    dni = models.CharField(max_length = 8, default="46037183")
    nombre = models.CharField(max_length = 30, default="Nombre")
    apellido = models.CharField(max_length = 30, default="Apellido")
    nacimiento = models.DateField(default= "2022-09-06")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1)
    direccion = models.ForeignKey(
        Direcciones,
        on_delete=models.CASCADE, default=1
    )

    telefono = models.CharField(max_length = 20, default="3513897259")
    ingresoEmpresa = models.DateFielddeadefault= ("2022-09-06")
    email = models.CharField(max_length = 40, default="mailfalso@gmail.com")
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE, default=1
    )
    def __str__(self):
        return f"{self.dni}, {self.nombre}, {self.apellido}"

class Turnos(models.Model):
    detalle = models.CharField(max_length=30)
    horaInicio = models.DateTimeField()
    horaFin = models.DateTimeField(null = True)
    cajero= models.ForeignKey(Cajero,on_delete=models.CASCADE, null=True,blank=True)
    turno_activo = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.horaInicio}, {self.horaFin}"
    class Meta:
        ordering = ("horaInicio", "horaFin")
        
class Asignaciones(models.Model):
    fechaInicio = models.DateField(default= "2022-09-06")
    fechaFin = models.DateField(default= "2022-09-06")
    listaDeCajas = models.ForeignKey(
        Cajas,
        on_delete=models.CASCADE, default=1
    )
    listaDeCajeros = models.ForeignKey(
        Cajero,
        on_delete=models.CASCADE, default=1
    )
    def __str__(self):
        return f"{self.fechaInicio}, {self.fechaFin}"
        
class Ventas(models.Model):
    fecha = models.DateField(default= "2022-09-06")
    listaDeAsignaciones = models.ForeignKey(
        Asignaciones,
        on_delete=models.CASCADE, default=1
    )
    def __str__(self):
        return f"{self.fecha}"

class Articulos(models.Model):
    codigo = models.IntegerField( default=123456)
    stock = models.IntegerField( default=1)
    nombre = models.CharField(max_length=50, default="Articulo")
    descripcion = models.CharField(max_length=200, default="Descripcion")
    precio = models.IntegerField( default=100)
    imagen = models.ImageField(null =True, blank=True, upload_to='images/')

    def __str__(self):
        return f"{self.stock}, {self.nombre}, {self.descripcion}, {self.precio}"


class detalleVentas(models.Model):
    numVenta = models.IntegerField( default=1234)
    numArticulo = models.IntegerField( default=1234)
    precioUnidad = models.IntegerField( default=1234)
    cantidad = models.IntegerField( default=1234)
    id_articulos = models.ForeignKey(
        Articulos,
        on_delete=models.CASCADE, default=1
    )
    id_ventas = models.ForeignKey(
        Ventas,
        on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return f"{self.precioUnidad}, {self.cantidad}"

