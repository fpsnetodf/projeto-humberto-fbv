from django.urls import path
from . import views

urlpatterns = [
    path('agendas/', views.lista_agendas, name='agendas'),
    path('agendas/nova/', views.criar_agenda, name='criar_agenda'),
    path('', views.dashboard, name='dashboard'),
    path('eleitores/', views.lista_eleitores, name='eleitores'),
    path('equipe/', views.equipe_view, name='equipe'),
    path('marketing/', views.marketing_view, name='marketing'),  # Define a URL
    path('contato/', views.contato, name='contato'),
]
