#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('layout', views.layout_page_view, name="layout"),
    path('about', views.about_page_view, name="about"),
    path('apresentacao', views.apresentacao_page_view, name="apresentacao"),
    path('competencias', views.competencias_page_view, name="competencias"),
    path('foramacao', views.formacao_page_view, name="formacao"),
    path('projetos', views.projetos_page_view, name="projetos"),
    path('licenciatura', views.licenciatura_page_view, name="licenciatura"),
    path('posts', views.posts_page_view, name="posts"),
    path('criar_post', views.criar_post_page_view, name="criar_post"),


]