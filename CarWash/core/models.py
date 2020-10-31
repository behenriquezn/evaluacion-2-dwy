from django.db import models

# Create your models here.

class TipoEmpleado(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo

class Empleado(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    nombreUsuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    nombreUsuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)

    def __str__(self):
        return self.rut

class Insumo(models.Model):
    nombre = models.CharField(max_length=12)
    precio = models.IntegerField(max_length=9)
    descripcion = models.CharField(max_length=300)
    stock = models.IntegerField(max_length=3)

    def __str__(self):
        return self.nombre



