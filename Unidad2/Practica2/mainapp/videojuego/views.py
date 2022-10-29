from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render

# Create your views here.
def videojuego_list(request):
    return render(request, "videojuego/videojuego_list.html")

def videojuego_form(request):
    return render(request, "videojuego/videojuego_form.html")

def videojuego_delete(request):
    return 