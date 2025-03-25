from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    # Resolve os conflitos com related_name personalizado
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Nome personalizado
        blank=True,
        help_text='Grupos aos quais o usuário pertence.',
        verbose_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Nome personalizado
        blank=True,
        help_text='Permissões específicas para este usuário.',
        verbose_name='permissões de usuário'
    )

    def __str__(self):
        return self.username

