from django.shortcuts import redirect, render
from .forms import PeliculaForm
from .models import Pelicula

# Create your views here.
def pelicula_list(request):
    context = {'pelicula_list': Pelicula.objects.all()}
    return render(request, "pelicula/pelicula_list.html", context)

def pelicula_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PeliculaForm()
        else:
            pelicula = Pelicula.objects.get(pk=id)
            form = PeliculaForm(instance=pelicula)

        return render(request, "pelicula/pelicula_form.html",{'form':form})
    else:
        if id == 0: 
            form = PeliculaForm(request.POST)
        else:
            pelicula = Pelicula.objects.get(pk=id)
            form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
        return redirect('/pelicula/lista')

def pelicula_delete(request, id):
    pelicula = Pelicula.objects.get(pk=id)
    pelicula.delete()
    return redirect('/pelicula/lista')