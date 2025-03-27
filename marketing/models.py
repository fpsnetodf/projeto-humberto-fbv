from django.db import models
from usuarios.models import CustomUser

class Midia(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('foto', 'Fotografia'),
        ('video', 'Vídeo'),
    ])
    arquivo = models.FileField(upload_to='midias/')
    data_criacao = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Relaciona com o usuário responsável

    def __str__(self):
        return self.titulo


class Postagem(models.Model):
    plataforma = models.CharField(max_length=50, choices=[
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
    ])
    texto = models.TextField()
    data_postagem = models.DateTimeField()
    criado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    arquivo = models.FileField(upload_to='marketing_materials/')
    responsavel = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='marketing_materials')  # Adicionando related_name

    def __str__(self):
        return self.nome
