from django.db import models
from Users.models import CustomUser

class Agenda(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('confirmada', 'Confirmada'),
            ('conflito', 'Conflito')
        ],
        default='pendente'
    )
    criado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    aprovado_por = models.ForeignKey(CustomUser, related_name='aprovacoes', on_delete=models.SET_NULL, null=True, blank=True)

    def is_conflicting(self):
        # Verifica se há conflitos na mesma data e horário
        return Agenda.objects.filter(data=self.data, horario=self.horario).exclude(id=self.id).exists()


