from django.shortcuts import render, redirect
from .models import Agenda

def lista_agendas(request):
    agendas = Agenda.objects.filter(criado_por=request.user)
    return render(request, 'campaign/lista_agendas.html', {'agendas': agendas})

def criar_agenda(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        Agenda.objects.create(
            titulo=titulo,
            descricao=descricao,
            data=data,
            horario=horario,
            criado_por=request.user
        )
        return redirect('lista_agendas')
    return render(request, 'campaign/criar_agenda.html')

