from django.db import models

# Create your models here.

class TipoAro (models.Model):
    nombreT= models.CharField(max_length=50)

    def __str__(self):
        return self.nombreT


class Aro (models.Model):
    nombre= models.CharField(max_length=90)
    color= models.CharField(max_length=30)
    tamaño= models.IntegerField()
    stock= models.IntegerField()
    tipoPin= models.CharField(max_length=20)
    tipoforma= models.ForeignKey(TipoAro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre