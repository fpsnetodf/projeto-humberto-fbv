from django import forms
from .models import Eleitor, Mensagem

class EleitorForm(forms.ModelForm):
    class Meta:
        model = Eleitor
        fields = ['nome', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Nome do Eleitor',
                'required': True
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Telefone (opcional)',
            }),
        }

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'contato', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Seu Nome',
                'required': True
            }),
            'contato': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Seu E-mail ou Telefone (opcional)',
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Digite sua mensagem aqui...',
                'rows': 5,
                'required': True
            }),
        }
