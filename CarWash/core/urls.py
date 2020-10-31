from django.urls import path
from .views import index, formulario, formularioInsumo, galeria, login, quienesSomos, ubicacion, agregarEmpleado, agregarInsumo, modificarEmpleado, modificarInsumo, eliminarEmpleado, eliminarInsumo



urlpatterns = [
    path('', index, name="index"),
    path('formulario/', formulario, name="formulario"),
    path('formularioInsumo/', formularioInsumo, name="formularioInsumo"),
    path('galeria/', galeria, name="galeria"),
    path('login/', login, name="login"),
    path('quienesSomos/', quienesSomos, name="quienesSomos"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('agregarEmpleado/', agregarEmpleado, name="agregarEmpleado"),
    path('agregarInsumo/', agregarInsumo, name="agregarInsumo"),
    path('modificarEmpleado/<id>', modificarEmpleado, name="modificarEmpleado"),
    path('modificarInsumo/<id>', modificarInsumo, name="modificarInsumo"),
    path('eliminarEmpleado/<id>',eliminarEmpleado, name="eliminarEmpleado"),
    path('eliminarInsumo/<id>',eliminarInsumo, name="eliminarInsumo"),

]

