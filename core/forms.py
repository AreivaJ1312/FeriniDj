from django  import forms
from django.forms import ModelForm
from .models import Aro, TipoAro,comunas,Contacto,sugerenciaConsulta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#validaciones
class AroForm(ModelForm):
    nombre= forms.CharField(min_length=2, max_length=90)
    color= forms.CharField(min_length=4, max_length=30)
    tamaño= forms.IntegerField(min_value=1, max_value=10)
    stock= forms.IntegerField(min_value=0, max_value=50)
    tipoPin= forms.CharField(min_length=3, max_length=20)

    class Meta:
        model = Aro
        fields = ['nombre','color','tamaño','stock','tipoPin','tipoforma','imagen']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']


class ContactForm(ModelForm):
    nombreC= forms.CharField( min_length=3,  max_length=90)
    apellido= forms.CharField(min_length=3,max_length=90)
    email= forms.EmailField (max_length = 254)
    sugerenciaConsulta= forms.CharField(max_length=10)
    comunas= forms.CharField(max_length=90)
    areaText= forms.CharField(max_length=300)

    class Meta:
        model = Contacto
        fields=['nombreC','apellido','email','sugCon','comuna','areaText']





