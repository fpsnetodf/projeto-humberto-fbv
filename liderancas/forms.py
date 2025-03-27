from django import forms
from .models import Lideranca

class LiderancaForm(forms.ModelForm):
    class Meta:
        model = Lideranca
        fields = ['nome', 'cargo', 'contato', 'meta']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Nome da Liderança',
                'required': True
            }),
            'cargo': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Cargo da Liderança'
            }),
            'contato': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Contato (E-mail ou Telefone)'
            }),
            'meta': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Meta (Ex.: 10, 20...)',
                'required': True
            }),
        }
