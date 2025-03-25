from django.urls import path
from . import views

urlpatterns = [
    path('agendas/', views.lista_agendas, name='lista_agendas'),
    path('agendas/nova/', views.criar_agenda, name='criar_agenda'),
]
