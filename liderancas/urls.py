from django.urls import path
from . import views

urlpatterns = [
    # Página inicial da lista de lideranças
    path('', views.lista_liderancas, name='lista_liderancas'),

    # Página para cadastrar uma nova liderança
    path('criar/', views.criar_lideranca, name='criar_lideranca'),

    # Página para visualizar os detalhes de uma liderança específica
    path('<int:id>/', views.detalhe_lideranca, name='detalhe_lideranca'),

    # Página para editar uma liderança existente
    path('<int:id>/editar/', views.editar_lideranca, name='editar_lideranca'),

    # Página para excluir uma liderança
    path('<int:id>/deletar/', views.deletar_lideranca, name='deletar_lideranca'),
]
