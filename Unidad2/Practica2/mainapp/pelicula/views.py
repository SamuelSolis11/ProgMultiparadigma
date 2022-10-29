from django.shortcuts import render
from .forms import PeliculaForm

# Create your views here.
def pelicula_list(request):
    return render(request, "pelicula/pelicula_list.html")

def pelicula_form(request):
    form = PeliculaForm()
    return render(request, "pelicula/pelicula_form.html",{'form':form})

def pelicula_delete(request):
    return 