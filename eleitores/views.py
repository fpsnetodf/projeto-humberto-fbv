
# views.py
from django.shortcuts import render
from .models import Eleitor

def lista_eleitores(request):
    eleitores = Eleitor.objects.all()
    return render(request, 'eleitores.html', {'eleitores': eleitores})