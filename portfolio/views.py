from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PostForm
from .models import Post
# Create your views here.

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



