from django import forms
from .models import Midia

class MidiaForm(forms.ModelForm):
    class Meta:
        model = Midia
        fields = ['titulo', 'tipo', 'arquivo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'placeholder': 'Título da Mídia'
            }),
            'tipo': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg'
            }),
            'arquivo': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg'
            }),
        }
