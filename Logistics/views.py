from django.shortcuts import render, redirect
from .models import MaterialCampanha, Transporte, Material, Rota
from django.contrib.auth.decorators import login_required
from .forms import MaterialForm
from datetime import datetime

# Lista de materiais
def lista_materiais(request):
    materiais = MaterialCampanha.objects.all()
    return render(request, 'materiais/lista_materiais.html', {'materiais': materiais})

@login_required
def lista_materiais(request):
    materiais = MaterialCampanha.objects.all()
    return render(request, 'logistica/lista_materiais.html', {'materiais': materiais})



# Cadastro de material
def cadastro_material(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        descricao = request.POST.get('descricao')
        MaterialCampanha.objects.create(
            nome=nome,
            quantidade=quantidade,
            descricao=descricao
        )
        return redirect('lista_materiais')
    return render(request, 'materiais/cadastro_material.html')

# Lista de transportes
def lista_transportes(request):
    transportes = Transporte.objects.all()
    return render(request, 'transporte/lista_transportes.html', {'transportes': transportes})

# Cadastro de transporte
def cadastro_transporte(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        capacidade = request.POST.get('capacidade')
        descricao = request.POST.get('descricao')
        Transporte.objects.create(
            tipo=tipo,
            capacidade=capacidade,
            descricao=descricao
        )
        return redirect('lista_transportes')
    return render(request, 'transporte/cadastro_transporte.html')

def lista_rotas(request):
    rotas = Rota.objects.all()
    return render(request, 'transporte/rotas.html', {'rotas': rotas})




@login_required
def adicionar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            if isinstance(material.data_criacao, str):  # Valida se é string
                material.data_criacao = datetime.strptime(material.data_criacao, '%Y-%m-%d').date()
            material.save()
            return redirect('lista_materiais')
    else:
        form = MaterialForm()
    return render(request, 'logistica/adicionar_material.html', {'form': form})

@login_required
def criar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            # Verifique e converta se necessário (caso o campo seja preenchido manualmente)
            if isinstance(material.data_criacao, str):
                try:
                    material.data_criacao = datetime.strptime(material.data_criacao, '%Y-%m-%d').date()
                except ValueError:
                    form.add_error('data_criacao', 'Formato de data inválido. Use YYYY-MM-DD.')
            material.save()
            return redirect('lista_materiais')
    else:
        form = MaterialForm()
    return render(request, 'logistica/criar_material.html', {'form': form})