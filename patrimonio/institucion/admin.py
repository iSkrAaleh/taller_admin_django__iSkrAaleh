from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion

#visualizacion paraver mejor los datos en forma de tabla
@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'año_fundacion')
    search_fields = ('nombre', 'ciudad')

@admin.register(GuiaMuseo)
class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'años_experiencia_guia', 'museo')
    list_filter = ('museo',)
    search_fields = ('nombre_completo',)

@admin.register(Exhibicion)
class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'guia')
    list_filter = ('tematica',)
    search_fields = ('titulo_exhibicion', 'tematica')
