from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_rotas, name='lista_rotas'),
    path('materiais/', views.lista_materiais, name='lista_materiais'),
    path('materiais/cadastro/', views.cadastro_material, name='cadastro_material'),
    path('transportes/', views.lista_transportes, name='lista_transportes'),
    path('transportes/cadastro/', views.cadastro_transporte, name='cadastro_transporte'),
]
