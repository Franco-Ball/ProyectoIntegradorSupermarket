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
admin.site.register(Turnos)
admin.site.register(Direcciones)
admin.site.register(Articulos)
admin.site.register(detalleVentas)
admin.site.register(Ventas)
admin.site.register(Asignaciones)
admin.site.register(Cajas)
admin.site.register(Sucursal)
admin.site.register(Cajero)