from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):

    class Meta:
        model = Videojuego
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'codigo': 'Codigo',
            'plataforma': 'Plataforma',
            'calificacion': 'Calificacion'
        }
        
   