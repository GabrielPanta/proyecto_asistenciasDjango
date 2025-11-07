from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'fecha', 'horas_trabajadas', 'mes', 'empresa')
    search_fields = ('dni', 'nombre')
    list_filter = ('empresa', 'mes')
