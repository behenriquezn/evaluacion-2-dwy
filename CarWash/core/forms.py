from django import forms
from django.forms import ModelForm
from .models import Empleado, Insumo

class EmpleadoForm(ModelForm):


    class Meta:
        model = Empleado
        fields = ['rut','nombre','apellido','email','tipo','nombreUsuario','contraseña']

class InsumoForm(ModelForm):


    class Meta:
        model = Insumo
        fields= ['nombre','precio','descripcion','stock']