# from django import forms
# from .models import MaterialCampanha

# class MaterialForm(forms.ModelForm):
#     class Meta:
#         model = MaterialCampanha
#         fields = ['nome', 'descricao', 'quantidade', 'tipo']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'descricao': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'quantidade': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'tipo': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'data_criacao': forms.DateInput(attrs={
#                 'class': 'w-full px-4 py-2 border rounded-lg',
#                 'type': 'date'  # Gera um seletor de data
#             }),
#         }
from django import forms
from .models import MaterialCampanha

class MaterialForm(forms.ModelForm):
    class Meta:
        model = MaterialCampanha
        fields = ['nome', 'descricao', 'quantidade', 'tipo']
        widgets = {
            'data_criacao': forms.DateInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg',
                'type': 'date',  # O tipo "date" força o navegador a gerar um seletor de datas
            }),
        }