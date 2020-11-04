from django.urls import path
from .views import home
from .views import aros

urlpatterns = [
    path('', home, name ="home"),
    path('aros', aros, name ="aros"),
]