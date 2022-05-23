from django.shortcuts import render

def pontuacao_quizz(request):
    pontuacao = 0

    if request.POST['p1'] == 'Nav':
        pontuacao+=1

    if request.POST['p2'] == 'Sup':
        pontuacao+=1

    if request.POST['p3'] == 'border-radius: 30px;':
        pontuacao+=1


    return pontuacao