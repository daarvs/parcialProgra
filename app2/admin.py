from django.contrib import admin
from .models import Proveedores, Productos,Sucursal

admin.site.register(Proveedores)
admin.site.register(Productos)
admin.site.register(Sucursal)