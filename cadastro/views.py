from django.shortcuts import render, redirect
from .models import Ciclo, Produto, Acabamento, Papel, Versao, Caderno
from django.http import HttpResponse


def cadastrar_ciclo(request):
    if request.method == 'GET':
        return render(request, 'cadastro_ciclo.html')
