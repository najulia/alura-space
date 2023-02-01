from django.db import models
from datetime import date

class Fotografia(models.Model):
    
    CATEGORIAS = [
        ("Nebulosa", "Nebulosa"),
        ("Estrela", "Estrela"),
        ("Galáxia", "Galáxia"),
        ("Planeta", "Planeta"),
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150)
    categoria = models.CharField(max_length = 100, choices=CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateField(default=date.today, blank=False)

    def __str__(self):
        return self.nome