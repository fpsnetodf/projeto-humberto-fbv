from django.db import models
from usuarios.models import CustomUser


import datetime

class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField()
    tipo = models.CharField(max_length=50, choices=[
        ('grafico', 'Material Gráfico'),
        ('outdoor', 'Outdoor'),
    ])
    data_disponivel = models.DateField()
    responsavel = models.ForeignKey('usuarios.CustomUser', on_delete=models.CASCADE, related_name='logistics_materials')

    def save(self, *args, **kwargs):
        if isinstance(self.data_disponivel, str):
            # Converter string no formato ISO para um objeto datetime.date
            self.data_disponivel = datetime.date.fromisoformat(self.data_disponivel)
        super(Material, self).save(*args, **kwargs)

class Transporte(models.Model):
    tipo = models.CharField(max_length=50)  # Ex.: Caminhão, Moto
    capacidade = models.IntegerField()  # Capacidade de carga
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - Capacidade: {self.capacidade} unidades"




class MaterialCampanha(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField()
    tipo = models.CharField(max_length=50, choices=[
        ('grafico', 'Material Gráfico'),
        ('outdoor', 'Outdoor'),
    ])
    data_criacao = models.DateField(auto_now_add=True)  # Configuração correta para preencher automaticamente na criação

    def __str__(self):
        return self.nome

class Rota(models.Model):
    origem = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    data = models.DateField()
    horario_partida = models.TimeField()
    horario_chegada = models.TimeField(blank=True, null=True)
    veiculo = models.CharField(max_length=100)
    responsavel = models.ForeignKey('usuarios.CustomUser', on_delete=models.CASCADE)
