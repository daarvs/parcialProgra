from django.shortcuts import render
from django.shortcuts import render,redirect
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from .formularios.ProveedorForm import ProveedorForm
from .formularios.ProductoForm import ProductoForm
from .formularios.SucursalForm import SucursalForm
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores,Sucursal
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = NewUserForm()
    return render(request, 'Reg_user.html', {'form': formulario})

@login_required(login_url='login')
def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()  
    es_admin = request.user.is_staff
    es_cajero = request.user.groups.filter(name='Cajero').exists()
    if es_estudiante or es_admin or es_cajero:
        return render(request,"index.html", {'user': request.user, 'es_estudiante': es_estudiante, 'es_admin': es_admin, 'es_cajero': es_cajero})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user =  authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def mostrar_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'mostrar_proveedores.html', {'proveedores': proveedores})

@user_passes_test(lambda u: u.is_staff, login_url='error_permisos') 
def agregar_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedores.html', {'form': form})


def mostrar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'mostrar_productos.html', {'productos': productos})

@user_passes_test(lambda u: u.is_staff, login_url='error_permisos') 
def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})



def mostrar_sucursales(request):
    sucursal = Sucursal.objects.all()
    return render(request, 'mostrar_sucursal.html', {'Sucursal': sucursal})

@user_passes_test(lambda u: u.is_staff, login_url='error_permisos') 
def agregar_sucursales(request):
    if request.method == "POST":
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_sucursales')
    else:
        form = SucursalForm()
    return render(request, 'agregar_sucursal.html', {'form': form})



def error_permisos(request):
    return render(request, 'error_permisos.html')
