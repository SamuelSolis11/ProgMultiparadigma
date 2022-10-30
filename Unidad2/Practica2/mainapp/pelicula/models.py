
from django.db import models

# Create your models here.

class Clasificacion(models.Model):
    titulo_cla = models.CharField(max_length=3)

    def __str__(self):
        return self.titulo_cla


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    genero = models.CharField(max_length=50)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo