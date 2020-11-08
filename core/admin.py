from django.contrib import admin
from .models import TipoAro, Aro, Contacto,sugerenciaConsulta,comunas

# Register your models here.

class AroAdmin (admin.ModelAdmin):
    list_display= ['nombre','color','tamaño','tipoPin','tipoforma','stock','imagen']
    search_fields= ['nombre','color','tamaño','tipoPin','stock']
    list_filter = ['tipoforma']
    list_per_page = 20

admin.site.register(TipoAro)
admin.site.register(Aro, AroAdmin)


class contactAdmin(admin.ModelAdmin):
    list_display= ['Nombre','apellido','email','sugCon','comuna','Mensaje']
    search_fields= ['Nombre','apellido','email','comuna']
    list_filter = ['sugCon']
    list_per_page = 20

admin.site.register(sugerenciaConsulta)
admin.site.register(Contacto,contactAdmin)
admin.site.register(comunas)