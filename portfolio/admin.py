from django.contrib import admin

# Register your models here.
from portfolio.models import *

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
admin.site.register(Projeto)
admin.site.register(Professor)
admin.site.register(Cadeira)
admin.site.register(Linguagem)
admin.site.register(Comentario)
admin.site.register(Pessoa)
admin.site.register(Tfc_terceiros)
admin.site.register(Tfc_autor)
admin.site.register(Tfc_orientador)

