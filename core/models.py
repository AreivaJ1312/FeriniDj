from django.db import models

# Create your models here.

class TipoAros(models.Model):
    #id
    forma= models.CharField(max_length=40) 
    # filtro (ovaldaos, corazon, etc) 

class Aros(models.Model):
    nombre= models.CharField(max_length=40)
    color= models.CharField(max_length=30)
    forma= models.ForeignKey(TipoAros, on_delete=models.CASCADE)
    tamaño= models.IntegerField()
    stock= models.IntegerField()
    tipoPin= models.IntegerField()

