from django.shortcuts import render, get_object_or_404, redirect
from .models import Lideranca
from .forms import LiderancaForm

# Lista de lideranças
def lista_liderancas(request):
    liderancas = Lideranca.objects.all()
    return render(request, 'lista_liderancas.html', {'liderancas': liderancas})

# Criar uma nova liderança
def criar_lideranca(request):
    if request.method == 'POST':
        form = LiderancaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_liderancas')
    else:
        form = LiderancaForm()
    return render(request, 'criar_lideranca.html', {'form': form})

# Detalhes de uma liderança específica
def detalhe_lideranca(request, id):
    lideranca = get_object_or_404(Lideranca, id=id)
    return render(request, 'detalhe_lideranca.html', {'lideranca': lideranca})

# Editar uma liderança existente
def editar_lideranca(request, id):
    lideranca = get_object_or_404(Lideranca, id=id)
    if request.method == 'POST':
        form = LiderancaForm(request.POST, instance=lideranca)
        if form.is_valid():
            form.save()
            return redirect('lista_liderancas')
    else:
        form = LiderancaForm(instance=lideranca)
    return render(request, 'editar_lideranca.html', {'form': form, 'lideranca': lideranca})

# Excluir uma liderança
def deletar_lideranca(request, id):
    lideranca = get_object_or_404(Lideranca, id=id)
    if request.method == 'POST':
        lideranca.delete()
        return redirect('lista_liderancas')
    return render(request, 'deletar_lideranca.html', {'lideranca': lideranca})

