from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Clasificacion(models.Model):
    titulo_cla = models.CharField(max_length=3)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    genero = models.CharField(max_length=50)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)