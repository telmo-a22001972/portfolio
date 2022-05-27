from django.forms import ModelForm

from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['comentarios']


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class ComentarioFrom(ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor', 'conteudo')


