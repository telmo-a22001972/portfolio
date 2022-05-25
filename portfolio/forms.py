from django.forms import ModelForm

from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'