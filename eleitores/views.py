
from django.shortcuts import render, get_object_or_404, redirect
from .models import Eleitor, Mensagem
from .forms import EleitorForm, MensagemForm

# Lista de eleitores
def lista_eleitores(request):
    eleitores = Eleitor.objects.all()
    return render(request, 'eleitores/eleitores.html', {'eleitores': eleitores})

# Criar um novo eleitor
def criar_eleitor(request):
    if request.method == 'POST':
        form = EleitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eleitores')
    else:
        form = EleitorForm()
    return render(request, 'eleitores/criar_eleitor.html', {'form': form})

# Detalhes de um eleitor específico
def detalhe_eleitor(request, id):
    eleitor = get_object_or_404(Eleitor, id=id)
    return render(request, 'eleitores/detalhe_eleitor.html', {'eleitor': eleitor})

# Editar dados de um eleitor
def editar_eleitor(request, id):
    eleitor = get_object_or_404(Eleitor, id=id)
    if request.method == 'POST':
        form = EleitorForm(request.POST, instance=eleitor)
        if form.is_valid():
            form.save()
            return redirect('lista_eleitores')
    else:
        form = EleitorForm(instance=eleitor)
    return render(request, 'eleitores/editar_eleitor.html', {'form': form, 'eleitor': eleitor})

# Excluir um eleitor
def deletar_eleitor(request, id):
    eleitor = get_object_or_404(Eleitor, id=id)
    if request.method == 'POST':
        eleitor.delete()
        return redirect('lista_eleitores')
    return render(request, 'eleitores/deletar_eleitor.html', {'eleitor': eleitor})

# Enviar mensagem ao candidato
def enviar_mensagem(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'eleitores/mensagem_sucesso.html')  # Página de sucesso
    else:
        form = MensagemForm()
    return render(request, 'eleitores/mensagem_candidato.html', {'form': form})


