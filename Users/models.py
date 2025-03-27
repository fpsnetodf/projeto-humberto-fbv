from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
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

    # Resolve os conflitos com related_name personalizado
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Nome único
        blank=True,
        help_text='Grupos aos quais o usuário pertence.',
        verbose_name='Grupos'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Nome único
        blank=True,
        help_text='Permissões específicas para este usuário.',
        verbose_name='Permissões de usuário'
    )

    def __str__(self):
        return self.nome_completo or self.username  # Retorna 'nome_completo', se disponível
