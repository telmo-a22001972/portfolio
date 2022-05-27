#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.about_page_view, name="about"),
    path('apresentacao', views.apresentacao_page_view, name="apresentacao"),
    path('competencias', views.competencias_page_view, name="competencias"),
    path('foramacao', views.formacao_page_view, name="formacao"),
    path('projetos', views.projetos_page_view, name="projetos"),
    path('posts', views.posts_page_view, name="posts"),
    path('criar_post', views.criar_post_page_view, name="criar_post"),
    path('editar_post/<int:post_id>', views.editar_post_page_view, name="editar_post"),
    path('web', views.web_page_view, name="web"),
    path('criar_cadeira', views.criar_cadeira_page_view, name="criar_cadeira"),
    path('criar_comentario/<int:post_id>/comentario', views.criar_comentario_page_view, name='criar_comentario'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),








]