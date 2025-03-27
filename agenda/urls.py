from django.urls import path
from . import views

urlpatterns = [
    # Página inicial da agenda
    path('', views.lista_agendas, name='lista_agendas'),
    
    # Página para criar uma nova agenda
    path('criar/', views.criar_agenda, name='criar_agenda'),
    
    # Página para visualizar detalhes de uma agenda específica
    path('<int:id>/', views.detalhe_agenda, name='detalhe_agenda'),
    
    # Página para editar uma agenda
    path('<int:id>/editar/', views.editar_agenda, name='editar_agenda'),
    
    # Página para deletar uma agenda
    path('<int:id>/deletar/', views.deletar_agenda, name='deletar_agenda'),
]
