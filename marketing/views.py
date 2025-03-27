from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Midia
from .forms import MidiaForm
from usuarios.models import CustomUser

# Lista de mídias
def lista_midias(request):
    midias = Midia.objects.all()
    return render(request, 'marketing/lista_midias.html', {'midias': midias})

# Upload de nova mídia

@login_required
def upload_midia(request):
    if request.method == 'POST':
        form = MidiaForm(request.POST, request.FILES)
        if form.is_valid():
            midia = form.save(commit=False)
            
            # Garante que o request.user é uma instância de CustomUser
            if isinstance(request.user, CustomUser):  # Verifica se já é um CustomUser
                midia.responsavel = request.user
            else:
                midia.responsavel = CustomUser.objects.get(id=request.user.id)  # Converte se necessário
            
            midia.save()
            return redirect('lista_midias')
    else:
        form = MidiaForm()
    return render(request, 'uploads/upload_midia.html', {'form': form})

# Detalhes de uma mídia específica
def detalhe_midia(request, id):
    midia = get_object_or_404(Midia, id=id)
    return render(request, 'marketing/detalhe_midia.html', {'midia': midia})

# Excluir uma mídia
def deletar_midia(request, id):
    midia = get_object_or_404(Midia, id=id)
    if request.method == 'POST':
        midia.delete()
        return redirect('lista_midias')
    return render(request, 'marketing/deletar_midia.html', {'midia': midia})

