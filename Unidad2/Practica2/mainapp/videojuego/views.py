from django.shortcuts import render, redirect
from .models import Videojuego
from .forms import VideojuegoForm


# Create your views here.
def videojuego_list(request):
    context = {'viedojuego_list': Videojuego.objects.all()}
    return render(request, "videojuego/videojuego_list.html", context)

def videojuego_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = VideojuegoForm()
        else:
            videojuego = Videojuego.objects.get(pk=id)
            form = VideojuegoForm(instance=videojuego)

        return render(request, "videojuego/videojuego_form.html",{'form':form})
    else:
        if id == 0: 
            form = VideojuegoForm(request.POST)
        else:
            videojuego  = Videojuego.objects.get(pk=id)
            form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
        return redirect('/videojuego/lista')

def videojuego_delete(request, id):
    videojuego = Videojuego.objects.get(pk=id)
    videojuego.delete()
    return redirect('/videojuego/lista')