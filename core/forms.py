from django  import forms
from django.forms import ModelForm
from .models import Aro, TipoAro


class AroForm(ModelForm):
    class Meta:
        model = Aro
        fields = ['nombre','color','tamaño','stock','tipoPin','tipoforma']