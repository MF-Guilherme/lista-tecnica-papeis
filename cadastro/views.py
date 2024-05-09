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


def cadastrar_versao(request):
    if request.method == 'GET':
        return render(request, 'cadastro_versao.html')
    elif request.method == 'POST':
        versao = request.POST.get('versao')

        nova_versao = Versao(nome=versao)
        nova_versao.save()
        messages.add_message(request, constants.SUCCESS, 'Versão cadastrada com sucesso!')
        return redirect('/cadastro/cadastrar_versao')


def cadastrar_acabamento(request):
    if request.method == 'GET':
        return render(request, 'cadastro_acabamento.html')
    elif request.method == 'POST':
        acabamento = request.POST.get('tipo_acabamento')

        novo_acabamento = Acabamento(tipo=acabamento)
        novo_acabamento.save()
        messages.add_message(request, constants.SUCCESS, 'Tipo de acabamento cadastrado com sucesso!')
        return redirect('/cadastro/cadastrar_acabamento')