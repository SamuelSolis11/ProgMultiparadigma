from django.shortcuts import render

# Create your views here.
def pelicula_list(request):
    return render(request, "pelicula/pelicula_list.html")

def pelicula_form(request):
    return render(request, "pelicula/pelicula_form.html")

def pelicula_delete(request):
    return 