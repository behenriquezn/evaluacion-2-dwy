from django.contrib import admin
from .models import TipoEmpleado, Empleado, Cliente, Insumo

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','apellido','email','tipo','nombreUsuario','contraseña']
    search_fields = ['rut']
    list_per_page = 10

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','apellido','email','nombreUsuario','contraseña']
    search_fields = ['rut']
    list_per_page = 10

class InsumoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','stock']
    search_fields = ['nombre']
    list_per_page = 10    

admin.site.register(TipoEmpleado)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Insumo, InsumoAdmin)