from django  import forms
from django.forms import ModelForm
from .models import Aro, TipoAro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

