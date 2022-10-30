from django.shortcuts import redirect, render
from .forms import DocumenrtalForm
from .models import Documental

# Create your views here.
def documental_list(request):
    context = {'documental_list': Documental.objects.all()}
    return render(request, "documental/documental_list.html", context)

def documental_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DocumenrtalForm()
        else:
            documental = Documental.objects.get(pk=id)
            form = DocumenrtalForm(instance=documental)

        return render(request, "documental/documental_form.html",{'form':form})
    else:
        if id == 0: 
            form = DocumenrtalForm(request.POST)
        else:
            documental = Documental.objects.get(pk=id)
            form = DocumenrtalForm(request.POST, instance=documental)
        if form.is_valid():
            form.save()
        return redirect('/documental/lista')

def documental_delete(request, id):
    documental = documental.objects.get(pk=id)
    documental.delete()
    return redirect('/documental/lista') 