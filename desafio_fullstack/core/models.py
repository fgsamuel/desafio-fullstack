from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE


class Estado(models.Model):
    sigla = models.CharField(max_length=2, unique=True, validators=[MinLengthValidator(2)])
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    estado = models.ForeignKey('Estado', on_delete=CASCADE, related_name='cidades')
    nome = models.CharField(max_length=200)

    class Meta:
        unique_together = ('estado', 'nome')
        ordering = ('estado__nome', 'nome')

    def __str__(self):
        return f'{self.nome} ({self.estado.sigla})'
