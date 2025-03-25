from django.db import models

class MaterialCampanha(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.quantidade}"

class Transporte(models.Model):
    tipo = models.CharField(max_length=50)  # Ex.: Caminhão, Moto
    capacidade = models.IntegerField()  # Capacidade de carga
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - Capacidade: {self.capacidade} unidades"



