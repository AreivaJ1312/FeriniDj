


from rest_framework import serializers
from .models import Aro,Contacto

class AroSerializaer(serializers.ModelSerializer):

    class Meta:
        model = Aro
        fields = ['nombre','color','tamaño', 'stock','tipoPin','tipoforma','imagen']


#AUN NO SE SI LO VOY A USAR PERO POR SIACASO
class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['Nombre','apellido','email','sugCon','comuna']