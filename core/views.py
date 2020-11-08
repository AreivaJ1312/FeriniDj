from django.shortcuts import render, redirect
from .models import Aro,TipoAro
from .forms  import AroForm
from .forms  import AroForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
# Create your views here.

def home(request):
    data={
        'aros':Aro.objects.all()
    }
    return render(request,'core/home.html',data)


def aros(request):
    data={
        'tipoAros':TipoAro.objects.all(),
        'aritos':Aro.objects.all()
    }
    return render(request,'core/aros.html',data)

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
        formulario = AroForm(request.POST, files=request.FILES)
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
        formulario = AroForm(data=request.POST, instance=aro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Modificado correctamente"
            data['form'] = AroForm(instance=Aro.objects.get(id=id))
  

    return render (request,'core/modificar_aro.html', data)  

def elimimar_aro(request,id):
    aro=Aro.objects.get(id=id)
    aro.delete()
    return redirect(to="ListadoAros")


def registro_usuario(request):
    data={
        'form':CustomUserForm()

    }
    if request.method =='POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario e ir al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request,user)
            return redirect(to='home')
    return render(request, 'registration/registrar.html',data)