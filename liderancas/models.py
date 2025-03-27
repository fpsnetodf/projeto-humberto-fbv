from django.db import models

class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    contato = models.CharField(max_length=50)
    meta = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

