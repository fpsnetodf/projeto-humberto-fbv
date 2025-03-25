from django.shortcuts import render, redirect
from .models import MaterialCampanha, Transporte

# Lista de materiais
def lista_materiais(request):
    materiais = MaterialCampanha.objects.all()
    return render(request, 'materiais/lista_materiais.html', {'materiais': materiais})

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
    return render(request, 'logistics/cadastro_transporte.html')

