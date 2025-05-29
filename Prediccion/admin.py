from django.contrib import admin
from Prediccion.models import Usuarios, Contacto


# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")


class ModeloContacto(admin.ModelAdmin):
    list_display = ("nombre", "correo", "mensaje")


admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Contacto, ModeloContacto)
