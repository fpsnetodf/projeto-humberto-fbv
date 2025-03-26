from django.urls import path
from . import views

urlpatterns = [
    path('eleitores/', views.lista_eleitores, name='lista_eleitores'),
]