from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm
from .models import *
# Create your views here.
from .quizz_functs import pontuacao_quizz


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def layout_page_view(request):
    return render(request, 'portfolio/layout.html')


def about_page_view(request):
    return render(request, 'portfolio/about.html')


def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_page_view(request):
    return render(request, 'portfolio')


def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


def posts_page_view(request):
    context = {'posts': sorted(Post.objects.all(), key=lambda objeto:objeto.criacao, reverse=True)}
    return render(request, 'portfolio/posts.html', context)


def criar_post_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')

    context = {'form':form}

    return render(request, 'portfolio/criar_post.html', context)



def web_page_view(request):
    if request.method == 'POST':
        name = request.POST['nome']+" "+request.POST['apelido']
        pontuacao = pontuacao_quizz(request)

        r = PontuacaoQuizz(nome = name, pontuacao=pontuacao)
        r.save()

    return render(request, 'portfolio/web.html')


def cadeiras(request):
    context = {'cadeiras': sorted(Cadeira.objects.all(), key=lambda cadeira: cadeira.nota, reverse=True)}
    return render(request, 'portfolio/cadeiras_temp.html', context)





