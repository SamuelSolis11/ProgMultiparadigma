from django.db import models

# Create your models here.


class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    plataforma = models.CharField(max_length=30)
    calificacion = models.CharField(max_length=3)

    def __str__(self):
        return self.titulo