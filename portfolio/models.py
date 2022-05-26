from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django import forms

# Para o campo não ser obrigatório mete-se ", blank= True"




class Post(models.Model):

    titulo = models.CharField(max_length=60)
    descricao = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo+" - "+self.autor


class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name="coments", on_delete=models.CASCADE)
    autor = models.CharField(max_length=20)
    conteudo = models.TextField()
    criacao_data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.autor)



class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()
    criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome+" : "+str(self.pontuacao)


class Linguagem(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=150, blank=True)
    universidade = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=20)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    nota = models.IntegerField()
    ects = models.IntegerField(default=0)
    ranking = models.IntegerField()
    linguagens = models.ManyToManyField(Linguagem, blank=True)
    professor_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    professor_pratica = models.ManyToManyField(Professor, related_name='professor_pratica')
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return f"{self.nome} - Professor: {self.professor_teorica}"




