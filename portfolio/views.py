from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *
from .models import *
# Create your views here.
from .quizz_functs import pontuacao_quizz


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def layout_page_view(request):
    return render(request, 'portfolio/layout.html')


def about_page_view(request):
    context = {'cadeiras': sorted(Cadeira.objects.all(), key=lambda cadeira: cadeira.ano and cadeira.semestre and cadeira.nota)}
    return render(request, 'portfolio/about.html', context)


def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_page_view(request):
    return render(request, 'portfolio')


def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')


def posts_page_view(request):
    context = {'posts': sorted(Post.objects.all(), key=lambda objeto:objeto.criacao, reverse=True)}
    return render(request, 'blog/posts.html', context)


def criar_post_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')

    context = {'form':form}

    return render(request, 'blog/criar_post.html', context)


def editar_post_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')

    context = {'form': form, 'post_id': post_id}

    return render(request, 'blog/editar_post.html', context)


def criar_comentario_page_view(request, post_id):
    form = ComentarioFrom(request.POST or None)
    post = Post.objects.get(pk=post_id)

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.save()

        return HttpResponseRedirect('/posts')

    context = {'form': form, 'post_id': post_id}
    return render(request, 'blog/criar_comentario.html', context)


def web_page_view(request):
    if request.method == 'POST':
        name = request.POST['nome']+" "+request.POST['apelido']
        pontuacao = pontuacao_quizz(request)

        r = PontuacaoQuizz(nome = name, pontuacao=pontuacao)
        r.save()

    return render(request, 'portfolio/web.html')


@login_required()
def criar_cadeira_page_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/about')

    context = {'form':form}

    return render(request, 'portfolio/criar_cadeira.html', context)


def login_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            return render(request, 'authenticate/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'authenticate/login.html')


def logout_page_view(request):
    logout(request)

    return render(request, 'portfolio/home.html', {
                'message': 'Foi desconetado.'
            })


