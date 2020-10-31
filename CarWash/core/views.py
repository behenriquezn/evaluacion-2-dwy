from django.shortcuts import render, redirect
from .models import Empleado, Insumo
from .forms import EmpleadoForm, InsumoForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def formulario(request):
    empleadoAll = Empleado.objects.all()
    datos = {
        'listaEmpleados' : empleadoAll
    }

    return render(request, 'core/formulario.html', datos)

def agregarEmpleado(request):
    datos = {
        'form' : EmpleadoForm()  

    }
    if request.method == 'POST':
        formu = EmpleadoForm(request.POST)
        if formu.is_valid():
            formu.save()
            datos['mensaje'] = "Empleado Guardado Correctamente"

    return render(request, 'core/agregarEmpleado.html', datos)

def modificarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    datos = {
        'form' : EmpleadoForm(instance=empleado)
    }
    if request.method == 'POST':
        formu = EmpleadoForm(data=request.POST, instance=empleado)
        if formu.is_valid():
            formu.save()
            datos['mensaje'] = "Empleado Modificado Correctamente"
            datos['form'] = formu

    return render(request, 'core/modificarEmpleado.html', datos)

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="formulario")



def formularioInsumo(request):
    insumosAll = Insumo.objects.all()
    datos = {
        'listaInsumos' : insumosAll
    }

    return render(request, 'core/formularioInsumo.html', datos)

def agregarInsumo(request):
    datos = {
        'form' : InsumoForm()  

    }
    if request.method == 'POST':
        formuIn = InsumoForm(request.POST)
        if formuIn.is_valid():
            formuIn.save()
            datos['mensaje'] = "Insumo Guardado Correctamente"

    return render(request, 'core/agregarInsumo.html', datos)

def modificarInsumo(request, id):
    insumo = Insumo.objects.get(id=id)
    datos = {
        'form' : InsumoForm(instance=insumo)
    }
    if request.method == 'POST':
        formuIn = InsumoForm(data=request.POST, instance=insumo)
        if formuIn.is_valid():
            formuIn.save()
            datos['mensaje'] = "Insumo Modificado Correctamente"
            datos['form'] = formuIn

    return render(request, 'core/modificarInsumos.html', datos)

def eliminarInsumo(request, id):
    insumo = Insumo.objects.get(id=id)
    insumo.delete()

    return redirect(to="formularioInsumo")

def galeria(request):
    return render(request, 'core/galeria.html')

def login(request):
    return render(request, 'core/login.html')

def quienesSomos(request):
    return render(request, 'core/quienesSomos.html')

def ubicacion(request):
    return render(request, 'core/ubicacion.html')



