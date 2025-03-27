from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):    
    nome_completo = models.CharField(
        max_length=150,
        verbose_name='Nome completo'
    )
    telefone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message='Número de telefone inválido. O formato deve conter até 15 dígitos e pode incluir "+" no início.'
        )],
        verbose_name='Telefone'
    )

    def __str__(self):
        return self.username
