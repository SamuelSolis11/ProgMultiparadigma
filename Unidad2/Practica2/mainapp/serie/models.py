from django.db import models

# Create your models here.
class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30)
    capitulos = models.CharField(max_length=5)
    calificacion = models.CharField(max_length=5)