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
    imagen = models.ImageField(null=True, blank =True)

    def __str__(self):
        return self.nombre


class sugerenciaConsulta(models.Model):
    nombreS= models.CharField(max_length=10)




class comunas(models.Model):
    nombreComuna= models.CharField(max_length=90)



class Contacto(models.Model):
    nombreC= models.CharField(max_length=90)
    apellido= models.CharField(max_length=90)
    email= models.EmailField (max_length = 254)
    sugCon= models.ForeignKey(sugerenciaConsulta, on_delete=models.CASCADE, default=None)
    comuna= models.ForeignKey(comunas, on_delete=models.CASCADE, default=None)
    areaText= models.CharField(max_length=300)


