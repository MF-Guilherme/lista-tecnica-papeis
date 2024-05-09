from django.shortcuts import render, redirect
from .models import Ciclo, Produto, Acabamento, Papel, Versao, Caderno
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants


def cadastrar_ciclo(request):
    if request.method == 'GET':
        return render(request, 'cadastro_ciclo.html')
    elif request.method == 'POST':
        ciclo = request.POST.get('ciclo')
        
        novo_ciclo = Ciclo(campanha=ciclo)
        novo_ciclo.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('/cadastro/cadastrar_ciclo')


