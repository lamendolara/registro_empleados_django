from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)


#Se define la visualización de esta tabla en Admin para visualizar los campos de la tabla.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )

    #De esta manera se agrega una concatenación de dos campos para formar un campo nuevo.
    #Muy util para realizar funciones y mostrarlas fácilmente por fuera de los campos del modelo.
    def full_name(self, obj):
        print(obj)
        return obj.first_name + ' ' + obj.last_name

    #Filtros para la tabla en admin
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')
    #El filtro horizontal funciona en la relacion many to many unicamente.
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
