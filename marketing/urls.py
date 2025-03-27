from django.urls import path
from . import views

urlpatterns = [
    # Página inicial da lista de mídias
    path('', views.lista_midias, name='lista_midias'),

    # Página para realizar o upload de nova mídia
    path('upload/', views.upload_midia, name='upload_midia'),

    # Página para visualizar detalhes de uma mídia específica
    path('<int:id>/', views.detalhe_midia, name='detalhe_midia'),

    # Página para deletar uma mídia
    path('<int:id>/deletar/', views.deletar_midia, name='deletar_midia'),
]
