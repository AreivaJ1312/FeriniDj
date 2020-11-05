from django.urls import path
from .views import home, aros, Contacto


urlpatterns = [
    path('', home, name ="home"),
    path('aros', aros, name ="aros"),
    path('Contacto', Contacto, name ="Contacto"),
]