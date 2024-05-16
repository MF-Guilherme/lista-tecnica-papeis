def desperdicio_discovery(tiragem):
    if tiragem <= 50000:
        return 2.0
    elif tiragem <= 100000:
        return 1.0
    else: 
        return 0.5
    

def desperdicio_refile(tiragem):    
    if tiragem < 25000:
        return (300/tiragem) * 100
    else:
        return 0.5
    

def desperdicio_tipo_acabamento(tipo, tiragem):
    if tiragem < 25000:
        return ((900 / tiragem)* 100)
    elif tipo == "Lombada Quadrada":
        return 2.0
    elif tipo == "Refile":
        return 0.5


def desperdicio_acerto_interno(tiragem, paginacao, exs_giro):
    if tiragem < 25000:
        if paginacao == 8:
            return 27000-tiragem
        else:
            return int((27000-tiragem) / exs_giro)
    else:
        if paginacao == 16 and exs_giro == 2:
            return 1000
        else:
            return 2000
        

def desperdicio_acerto_cliente(tiragem, paginacao, exs_giro):
    if tiragem < 25000:
        return desperdicio_acerto_interno(tiragem, paginacao, exs_giro)
    else:
        return 2000


def desperdicio_imp_interno(disc_imp, refile_imp, desintercalacao, paginacao, tiragem):
    desp_discovery = 0.0
    desp_refile = 0.0
    desp_desintercalacao = 0.0
    desp_caderno = 0.0

    if disc_imp == '1':
        desp_discovery = desperdicio_discovery(tiragem)
    
    if refile_imp == '1':
        desp_refile = desperdicio_refile(tiragem)

    if desintercalacao == '1':
        desp_desintercalacao = 0.2
    
    if paginacao < 24:
        desp_caderno = 6.0
    else:
        desp_caderno = 8.0
    
    total = desp_caderno + desp_discovery + desp_refile + desp_desintercalacao
    
    return total


def desperdicio_acbto_interno(tiragem, tipo_acbto, refile, discovery, disc_man):
    desp_acbto = desperdicio_tipo_acabamento(tipo_acbto, tiragem)
    desp_refile = 0.0
    desp_discovery = 0.0
    desp_disc_man = 0.0

    if refile == '1':
        desp_refile = desperdicio_refile(tiragem)
    if discovery == '1':
        desp_discovery = desperdicio_discovery(tiragem)
    if disc_man == '1':
        desp_disc_man = desperdicio_discovery(tiragem)

    total = desp_acbto + desp_refile + desp_discovery + desp_disc_man

    return total


def valores_por_caderno(lista_de_cadernos):
    lista_valores = []
    for caderno in lista_de_cadernos:
        lista_valores.append(list(caderno.values()))
    return lista_valores


def salvar_caderno(lista_de_valores, tiragem, tipo_acabamento):
    try:
        for cad in lista_de_valores:
            nome = cad[0]
            paginacao = int(cad[1])
            exs_giro = int(cad[2])
            papel = cad[3]
            disc_imp = cad[4]
            refile_imp = cad[5]
            desintercalacao = cad[6]
            refile_acab = cad[7]
            disc_acab = cad[8]
            disc_manual = cad[9]

            desp_acerto_int = desperdicio_acerto_interno(tiragem, paginacao, exs_giro)
            desp_impressao_int = desperdicio_imp_interno(disc_imp, refile_imp, desintercalacao, paginacao, tiragem)
            desp_acabamento_int = desperdicio_acbto_interno(tiragem, tipo_acabamento, refile_acab, disc_acab, disc_manual)
            
            return nome, paginacao, exs_giro, papel, disc_imp, refile_imp, desintercalacao, refile_acab, disc_acab, disc_manual, desp_acerto_int, desp_impressao_int, desp_acabamento_int
            # print(f'Caderno {i+1}')
            # print(nome, paginacao, exs_giro, papel, disc_imp, refile_imp, desintercalacao, refile_acab, disc_acab, disc_manual)
            # print(f'Acerto: {desp_acerto_int}\n'
            #     f'Impressão: {desp_impressao_int}\n'
            #     f'Acabamento: {desp_acabamento_int}')
            # caderno = Caderno(nome=nome, paginacao=paginacao,)
    except Exception as e:
        print(str(e))



if __name__ == "__main__":

    #print(desperdicio_acbto_interno(100001, 'Lombada Quadrada', 1, None, None))

    
    lista = [
        {'nome_caderno_1': '01 cad', 'paginacao_1': '32', 'exs_giro_1': '1', 'papel_1': '2', 'disc_imp_1': '1', 'refile_imp_1': '1', 'desintercalacao_1': '1', 'refile_acab_1': '0', 'disc_acab_1': '0', 'disc_man_1': '0'}, 
        {'nome_caderno_2': '02 cad', 'paginacao_2': '28', 'exs_giro_2': '1', 'papel_2': '3', 'disc_imp_2': '0', 'refile_imp_2': '0', 'desintercalacao_2': '0', 'refile_acab_2': '1', 'disc_acab_2': '1', 'disc_man_2': '1'}
        ]
    
    lista_valores = valores_por_caderno(lista)
    valores_caderno = salvar_caderno(lista_valores, 460810, 'Lombada Quadrada')

    # print(valores_caderno)


        
            
                            


