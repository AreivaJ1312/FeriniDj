from django.urls import path
from .views import home, aros, Contacto, ListadoAros, nuevo_aro,modificar_aro, elimimar_aro


urlpatterns = [
    path('', home, name ="home"),
    path('aros', aros, name ="aros"),
    path('Contacto', Contacto, name ="Contacto"),
    path('ListadoAros',ListadoAros ,name= "ListadoAros" ),
    path('nuevo_aro', nuevo_aro, name= "nuevo_aro"),
    path('modificar_aro/<id>', modificar_aro, name="modificar_aro"),
    path('eliminar_aro/<id>',elimimar_aro, name="eliminar_aro"),
]