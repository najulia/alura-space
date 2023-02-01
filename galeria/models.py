from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150)
    descricao = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome