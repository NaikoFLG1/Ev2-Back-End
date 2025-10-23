from django.contrib import admin

# Register your models here.exi
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'fecha_ingreso', 'ubicacion')
