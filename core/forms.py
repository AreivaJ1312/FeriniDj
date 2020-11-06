from django  import forms
from django.forms import ModelForm
from .models import Aro


class AroForm(ModelForm):
    class Meta:
        model = Aro
        fields = ['nombre','color','tamaño','stock','tipoPin','tipoforma']