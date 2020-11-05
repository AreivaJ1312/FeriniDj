from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')


def aros(request):
    return render(request,'core/aros.html')

def Contacto(request):
    return render(request,'core/Contacto.html')