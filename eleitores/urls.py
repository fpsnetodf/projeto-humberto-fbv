from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('eleitores/', views.lista_eleitores, name='lista_eleitores'),
]
=======
    # Página inicial da lista de eleitores
    path('', views.lista_eleitores, name='lista_eleitores'),
    
    # Página para cadastrar um novo eleitor
    path('criar/', views.criar_eleitor, name='criar_eleitor'),
    
    # Página para visualizar detalhes de um eleitor específico
    path('<int:id>/', views.detalhe_eleitor, name='detalhe_eleitor'),
    
    # Página para editar os dados de um eleitor
    path('<int:id>/editar/', views.editar_eleitor, name='editar_eleitor'),
    
    # Página para excluir um eleitor
    path('<int:id>/deletar/', views.deletar_eleitor, name='deletar_eleitor'),
    
    # Página para enviar uma mensagem ao candidato
    path('mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]
>>>>>>> abc5463 (ajustanto templates)
