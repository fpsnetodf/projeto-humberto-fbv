from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Agenda, Usuario

@login_required
def lista_agendas(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirecione para a página de login

    agendas = Agenda.objects.filter(criado_por=request.user)
    return render(request, 'agenda/agenda_list.html', {'agendas': agendas})


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



@login_required
def nova_agenda(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        data_str = request.POST.get("data")
        tipo = request.POST.get("tipo")

        # Converte a data corretamente
        from django.utils.dateparse import parse_datetime
        data = parse_datetime(data_str)
        if data is None:
            return HttpResponse("Formato de data inválido. Use YYYY-MM-DD HH:MM", status=400)

        # Garante que o usuário autenticado seja usado
        usuario = request.user
        if not isinstance(usuario, Usuario):
            return HttpResponse("Erro de autenticação. Faça login novamente.", status=403)

        # Criando o objeto da agenda
        Agenda.objects.create(
            titulo=titulo,
            descricao=descricao,
            data=data,
            tipo=tipo,
            criado_por=usuario
        )
        return redirect("dashboard")

    return render(request, "nova_agenda.html")

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def lista_eleitores(request):
    return render(request, 'eleitores.html')  # Certifique-se que este template existe


def equipe_view(request):
    return render(request, 'equipe.html')  # Certifique-se que este template existe


def marketing_view(request):
    return render(request, 'marketing.html')  # Certifique-se que o template existe