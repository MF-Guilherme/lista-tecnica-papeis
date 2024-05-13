from django.shortcuts import render, redirect
from .models import Ciclo, Produto, Acabamento, Papel, Versao, Caderno
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.messages import constants
from .utils import desperdicio_acerto_interno, desperdicio_imp_interno, desperdicio_acbto_interno
import json


def cadastrar_ciclo(request):
    if request.method == 'GET':
        ultimo_ciclo = Ciclo.objects.latest('id')
        return render(request, 'cadastro_ciclo.html', {'ultimo_ciclo': ultimo_ciclo})
    elif request.method == 'POST':
        ciclo = request.POST.get('ciclo')
        
        novo_ciclo = Ciclo(campanha=ciclo)
        novo_ciclo.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('/cadastro/cadastrar_ciclo')


def cadastrar_versao(request):
    if request.method == 'GET':
        versoes = Versao.objects.all()
        return render(request, 'cadastro_versao.html', {'versoes': versoes})
    elif request.method == 'POST':
        versao = request.POST.get('versao')

        nova_versao = Versao(nome=versao)
        nova_versao.save()
        messages.add_message(request, constants.SUCCESS, 'Versão cadastrada com sucesso!')
        return redirect('/cadastro/cadastrar_versao')


def cadastrar_acabamento(request):
    if request.method == 'GET':
        tipos_acabamento = Acabamento.objects.all()
        return render(request, 'cadastro_acabamento.html', {'tipos_acabamento': tipos_acabamento})
    elif request.method == 'POST':
        acabamento = request.POST.get('tipo_acabamento')

        novo_acabamento = Acabamento(tipo=acabamento)
        novo_acabamento.save()
        messages.add_message(request, constants.SUCCESS, 'Tipo de acabamento cadastrado com sucesso!')
        return redirect('/cadastro/cadastrar_acabamento')
    

def cadastrar_papel(request):
    if request.method == 'GET':
        papeis = Papel.objects.all()
        return render(request, 'cadastro_papel.html', {'papeis': papeis})
    elif request.method == 'POST':
        codigo = request.POST.get('codigo')
        gramatura = int(request.POST.get('gramatura'))
        bobina = int(request.POST.get('bobina'))
        tipo = request.POST['tipo']

        descricao = f'{tipo} {gramatura}x{bobina}mm'

        cutoff = 0
        if bobina < 500:
            cutoff = 584
        elif bobina <= 940:
            cutoff = 578
        else:
            cutoff = 546

        try:
            papel = Papel(
                codigo=codigo,
                descricao=descricao,
                gramatura=gramatura,
                bobina=bobina,
                cutoff=cutoff
            )
            papel.save()
            messages.add_message(request, constants.SUCCESS, 'Papel cadastrado com sucesso!')
            return redirect('/cadastro/cadastrar_papel')
        except:
            messages.add_message(request, constants.ERROR, 'Cadastro não realizado, por favor revise as informações')
            return redirect('/cadastro/cadastrar_papel')
        

def cadastrar_lista_tecnica(request):
    if request.method == 'GET':
        ciclos = Ciclo.objects.all()
        versoes = Versao.objects.all()
        tipos_acbto = Acabamento.objects.all()
        papeis = Papel.objects.all()
        return render(request, 'cadastro_lista_tecnica.html', {'ciclos': ciclos, 'versoes': versoes, 'tipos_acbto': tipos_acbto, 'papeis': papeis})
    elif request.method == 'POST':
        # tiragem = 100001
        # tipo_acbto = "Lombada Quadrada"
        # nome_caderno = request.POST.get('nome_caderno')
        # paginacao = int(request.POST.get('paginacao'))
        # exs_giro = int(request.POST.get('exs_giro'))
        # papel = int(request.POST.get('papel'))
        # disc_imp = request.POST.get('disc_imp')
        # refile_imp = request.POST.get('refile_imp')
        # desintercalacao = request.POST.get('desintercalacao')
        # refile_acab = request.POST.get('refile_acab')
        # disc_acab = request.POST.get('disc_acab')
        # disc_man = request.POST.get('disc_man')
               
        # desp_acerto_int = desperdicio_acerto_interno(tiragem, paginacao, exs_giro)
        # desp_imp_int = desperdicio_imp_interno(disc_imp, refile_imp, desintercalacao, paginacao, tiragem)
        # desp_acbto_int = desperdicio_acbto_interno(tiragem, tipo_acbto, refile_acab, disc_acab, disc_man)

        # print(f'Entrada = {desp_acerto_int}')
        # print(f'Impressão = {desp_imp_int}')
        # print(f'Acabamento = {desp_acbto_int}')
        formData = request.POST
        table_data = json.loads(formData['table_data'])

        # Agora você pode acessar os dados da tabela em 'table_data'
        print(table_data)

        # Suponha que o redirecionamento seja para '/cadastro/cadastrar_lista_tecnica/'
        # Você pode alterar a URL conforme necessário
        redirect_url = '/cadastro/cadastrar_lista_tecnica/'

        # Retorna uma resposta JSON indicando que a operação foi bem-sucedida
        return JsonResponse({'success': True, 'redirect_url': redirect_url})