from django.db import models

# Create your models here.
class Eleitor(models.Model):

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome




# class Mensagem(models.Model):
#     nome = models.CharField(max_length=100)
#     contato = models.CharField(max_length=50, blank=True, null=True)  # E-mail ou telefone opcional
#     mensagem = models.TextField()
#     data_envio = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Mensagem de {self.nome} em {self.data_envio.strftime('%d/%m/%Y')}"
class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=50, blank=True, null=True)  # E-mail ou telefone opcional
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} em {self.data_envio.strftime('%d/%m/%Y')}"

