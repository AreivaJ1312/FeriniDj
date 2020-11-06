from django.urls import path
from .views import home, aros, Contacto, ListadoAros, nuevo_aro


urlpatterns = [
    path('', home, name ="home"),
    path('aros', aros, name ="aros"),
    path('Contacto', Contacto, name ="Contacto"),
    path('ListadoAros',ListadoAros ,name= "ListadoAros" ),
    path('nuevo_aro', nuevo_aro, name= "nuevo_aro"),
]