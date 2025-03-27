from django.shortcuts import render, get_object_or_404, redirect
from .models import Agenda

# Listar todas as agendas
def lista_agendas(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda/lista_agendas.html', {'agendas': agendas})

# Criar uma nova agenda
def criar_agenda(request):
    if request.method == 'POST':
        # Lógica para criar a agenda
        pass
    return render(request, 'agenda/criar_agenda.html')

# Detalhes de uma agenda específica
def detalhe_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    return render(request, 'agenda/detalhe_agenda.html', {'agenda': agenda})

# Editar uma agenda existente
def editar_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    if request.method == 'POST':
        # Lógica para editar a agenda
        pass
    return render(request, 'agenda/editar_agenda.html', {'agenda': agenda})

# Deletar uma agenda
def deletar_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    if request.method == 'POST':
        agenda.delete()
        return redirect('lista_agendas')
    return render(request, 'agenda/deletar_agenda.html', {'agenda': agenda})
