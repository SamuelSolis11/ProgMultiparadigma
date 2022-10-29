from cProfile import label
from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'codigo': 'Codigo',
            'genero': 'Genero',
            'clasificacion': 'Clasificacion'
        }
