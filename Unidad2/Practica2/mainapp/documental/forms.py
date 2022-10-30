from django import forms
from .models import Documental

class DocumenrtalForm(forms.ModelForm):

    class Meta:
        model = Documental
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'codigo': 'Codigo',
            'genero': 'Genero',
            'clasificacion': 'Clasificacion'
        }
        
    def __init__(self, *args, **kwargs):
        super(DocumenrtalForm, self).__init__(*args, **kwargs)
        self.fields['clasificacion'].empty_label = "-- Seleccionar --"
