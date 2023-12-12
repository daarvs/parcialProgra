"""
URL configuration for actividad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app2 import views as ap2v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ap2v.index, name='home'),
    path('registro/', ap2v.reg_user, name='registro'),
    path('login/', ap2v.iniciar_sesion, name='login'),  
    path('logout/', ap2v.cerrar_sesion, name='logout'),
    path('mostrar_proveedores/', ap2v.mostrar_proveedores, name='mostrar_proveedores'),
    path('agregar_proveedor/', ap2v.agregar_proveedor, name='agregar_proveedor'),
    path('mostrar_productos/', ap2v.mostrar_productos, name='mostrar_productos'),
    path('agregar_producto/', ap2v.agregar_producto, name='agregar_producto'),
    path('error_permisos/', ap2v.error_permisos, name='error_permisos'),
    path('agregar_sucursales/', ap2v.agregar_sucursales, name='agregar_sucursales'),
    path('mostrar_sucursales/', ap2v.mostrar_sucursales, name='mostrar_sucursales')
]
