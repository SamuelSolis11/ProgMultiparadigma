from django.shortcuts import render, redirect
from .models import Serie
from .forms import SerieForm


# Create your views here.
def serie_list(request):
    context = {'serie_list': Serie.objects.all()}
    return render(request, "serie/serie_list.html", context)

def serie_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SerieForm()
        else:
            serie = Serie.objects.get(pk=id)
            form = SerieForm(instance=serie)

        return render(request, "serie/serie_form.html",{'form':form})
    else:
        if id == 0: 
            form = SerieForm(request.POST)
        else:
            serie  = Serie.objects.get(pk=id)
            form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
        return redirect('/serie/lista')

def serie_delete(request, id):
    serie = Serie.objects.get(pk=id)
    serie.delete()
    return redirect('/serie/lista')