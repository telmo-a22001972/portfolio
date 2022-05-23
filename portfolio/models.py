from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django import forms


class Post(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=500)
    criacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=20)



    def __str__(self):
        return self.autor+": " +self.titulo + " - " + self.descricao[:30]

class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()
    criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome+" : "+str(self.pontuacao)