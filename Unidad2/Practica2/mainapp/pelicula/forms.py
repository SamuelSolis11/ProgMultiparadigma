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
        
    def __init__(self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields['clasificacion'].empty_label = "-- Seleccionar --"


    
