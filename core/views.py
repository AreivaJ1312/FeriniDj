from django.shortcuts import render
from .models import Aro

# Create your views here.

def home(request):
    return render(request,'core/home.html')


def aros(request):
    return render(request,'core/aros.html')

def Contacto(request):
    return render(request,'core/Contacto.html')

def ListadoAros(request):
    aros_= Aro.objects.all()
    data ={
        'aros_':aros_
    }

    return render(request, 'core/ListadoAros.html', data)