from django.db import models
from usuarios.models import CustomUser

class Agenda(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('conflito', 'Conflito')
    ])
    criado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='agendas_criadas')
