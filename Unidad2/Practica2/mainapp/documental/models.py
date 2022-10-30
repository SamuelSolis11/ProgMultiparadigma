from django.db import models
from pelicula.models import Clasificacion

# Create your models here.


class Documental(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    genero = models.CharField(max_length=50)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
