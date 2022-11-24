from django.contrib import admin

from .models import Turnos
from .models import Direcciones
from .models import Articulos
from .models import detalleVentas
from .models import Ventas
from .models import Asignaciones
from .models import Cajas
from .models import Sucursal
from .models import Cajero




# Register your models here.
class TurnosAdmin(admin.ModelAdmin):
    list_display = ("horaInicio", "horaFin")
    list_filter = ("horaInicio", )

admin.site.register(Turnos, TurnosAdmin)

class DireccionesAdmin(admin.ModelAdmin):
    list_display = ("calle", "altura")
admin.site.register(Direcciones, DireccionesAdmin)

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "stock", "precio")
    search_fields = ("nombre__startswith", )
admin.site.register(Articulos, ArticulosAdmin)

class DetalleAdmin(admin.ModelAdmin):
    list_display = ("precioUnidad", "cantidad")
admin.site.register(detalleVentas, DetalleAdmin)

class VentasAdmin(admin.ModelAdmin):
    list_display = ("fecha", "listaDetalleVenta")
admin.site.register(Ventas, VentasAdmin)

class AsignacionesAdmin(admin.ModelAdmin):
    list_display = ("fechaInicio", "fechaFin")
admin.site.register(Asignaciones, AsignacionesAdmin)

class CajasAdmin(admin.ModelAdmin):
    list_display = ("estado", "listaDeAsignacion")
admin.site.register(Cajas, CajasAdmin)

class SucursalAdmin(admin.ModelAdmin):
    list_display = ("telefono", "listaDeCaja", "direccion")
admin.site.register(Sucursal, SucursalAdmin)

class CajeroAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombre", "apellido", "direccion", "sucursal", "turnoTrabajo")
admin.site.register(Cajero, CajeroAdmin)