from django.contrib import admin
from .models import Pelicula, Clasificacion

# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Clasificacion)