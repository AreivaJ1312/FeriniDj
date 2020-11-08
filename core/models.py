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
    def __str__(self):
        return self.nombreS



class comunas(models.Model):
    nombreComuna= models.CharField(max_length=90)
    def __str__(self):
        return self.nombreComuna



class Contacto(models.Model):
    Nombre= models.CharField(max_length=90, verbose_name="Ingrese su Nombre")
    apellido= models.CharField(max_length=90)
    email= models.EmailField (max_length = 254)
    sugCon= models.ForeignKey(sugerenciaConsulta, on_delete=models.CASCADE, default=None,verbose_name="Sugerencia o Consulta")
    comuna= models.ForeignKey(comunas, on_delete=models.CASCADE, default=None, verbose_name="Comuna")
    Mensaje= models.CharField(max_length=300,verbose_name= "Mensaje")
    def __str__(self):
        return self.Nombre



