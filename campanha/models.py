from django.db import models
from Users.models import CustomUser

class Agenda(models.Model):
    # Usuário associado à agenda
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='agendas_associadas',  # Nome personalizado único
        verbose_name='Usuário associado'
    )

    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data = models.DateField(verbose_name='Data')
    horario = models.TimeField(verbose_name='Horário')

    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('confirmada', 'Confirmada'),
            ('conflito', 'Conflito')
        ],
        default='pendente',
        verbose_name='Status'
    )

    # Criador da agenda
    criado_por = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='agendas_criadas',  # Nome personalizado único
        verbose_name='Criado por'
    )

    # Usuário que aprovou a agenda
    aprovado_por = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        related_name='agendas_aprovadas',  # Nome único para evitar conflitos
        null=True,
        blank=True,
        verbose_name='Aprovado por'
    )

    def __str__(self):
        return self.titulo


    def is_conflicting(self):
        # Verifica se há conflitos na mesma data e horário
        return Agenda.objects.filter(data=self.data, horario=self.horario).exclude(id=self.id).exists()



