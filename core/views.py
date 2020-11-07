from django.shortcuts import render, redirect
from .models import Aro,TipoAro
from .forms  import AroForm

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

def nuevo_aro(request):
    data ={
        'form': AroForm()
    }

    if request.method =='POST':
        formulario = AroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
    return render(request,'core/nuevo_aro.html',data)



def modificar_aro(request, id):
    aro= Aro.objects.get(id=id)
    data = {
        'form': AroForm(instance=aro)
    }
    if request.method =='POST':
        formulario = AroForm(data=request.POST, instance=aro)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Modificado correctamente"
            data['form'] = formulario
  

    return render (request,'core/modificar_aro.html', data)  

def elimimar_aro(request,id):
    aro=Aro.objects.get(id=id)
    aro.delete()
    return redirect(to="ListadoAros")


