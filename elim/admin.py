from django.contrib import admin
from .forms import ServicioForm
# Register your models here.

from .models import Persona,\
    Cliente,Vehiculo,Conductor,\
        Trayecto,Programador,Servicio ,\
            Pais, Museo, Registro, Locations
            
class TrayectoAdmin(admin.ModelAdmin):
    search_fields = ('direccion'),
    ordering = ['direccion']

class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    #form = ServicioForm

class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ('placa'),
    ordering = ['placa']
    list_display = ['placa','tipo','conductor','estado','hora','disponibilidad','mecanico','restaurante','enfermo']

class ConductorAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']
    
class ProgramadorAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']

class ServicioAdmin(admin.ModelAdmin):   
    autocomplete_fields = ['placa','cliente','trayecto','solicitado_por','programador']  #,'trayecto','solicitado_por','programador']
    ordering = ['-fc']
    list_display = ['placa','fc','cliente','medio_pago','trayecto','valor','costo','neto','status','solicitado_por','programador']


class PaisAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']


class MuseoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pais']
    ordering = ['nombre']


class RegistroAdmin(admin.ModelAdmin):
    autocomplete_fields = ['cliente','placa','trayecto']
    list_display = ['placa','trayecto']
    ordering = ['-fecha']

admin.site.register(Pais, PaisAdmin)
admin.site.register(Museo, MuseoAdmin)


admin.site.register(Registro, RegistroAdmin)
admin.site.register(Trayecto, TrayectoAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Conductor,ConductorAdmin)
admin.site.register(Programador,ProgramadorAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Locations)