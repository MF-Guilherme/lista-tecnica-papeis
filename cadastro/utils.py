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


def desperdicio_imp_interno(disc_imp, refile_imp, desintercalacao, paginacao, tiragem):
    desp_discovery = 0.0
    desp_refile = 0.0
    desp_desintercalacao = 0.0
    desp_caderno = 0.0

    if disc_imp:
        desp_discovery = desperdicio_discovery(tiragem)
    
    if refile_imp:
        desp_refile = desperdicio_refile(tiragem)

    if desintercalacao:
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

    if refile:
        desp_refile = desperdicio_refile(tiragem)
    if discovery:
        desp_discovery = desperdicio_discovery(tiragem)
    if disc_man:
        desp_disc_man = desperdicio_discovery(tiragem)

    total = desp_acbto + desp_refile + desp_discovery + desp_disc_man

    return total



if __name__ == "__main__":

    #print(desperdicio_acbto_interno(100001, 'Lombada Quadrada', 1, None, None))

    
    lista = [
        {'nome_caderno_1': '01 cad', 'paginacao_1': '32', 'exs_giro_1': '1', 'papel_1': '2', 'disc_imp_1': '1', 'refile_imp_1': '1', 'desintercalacao_1': '1', 'refile_acab_1': '0', 'disc_acab_1': '0', 'disc_man_1': '0'}, 
        {'nome_caderno_2': '02 cad', 'paginacao_2': '28', 'exs_giro_2': '1', 'papel_2': '3', 'disc_imp_2': '0', 'refile_imp_2': '0', 'desintercalacao_2': '0', 'refile_acab_2': '1', 'disc_acab_2': '1', 'disc_man_2': '1'}
        ]
    


    for i, dic in enumerate(lista):
        nome_cad = dic.get(f'nome_caderno_{str(i+1)}')
        paginacao = dic.get(f'paginacao_{str(i+1)}')
        exs_giro = dic.get(f'exs_giro_{str(i+1)}')
        papel = dic.get(f'papel_{str(i+1)}')
        disc_imp = dic.get(f'disc_imp_{str(i+1)}')
        refile_imp = dic.get(f'refile_imp_{str(i+1)}')
        desintercalacao = dic.get(f'desintercalacao_{str(i+1)}')
        refile_acabamento = dic.get(f'refile_acab_{str(i+1)}')
        disc_acabamento = dic.get(f'disc_acab_{str(i+1)}')
        disc_manual = dic.get(f'disc_man_{str(i+1)}')
        print(nome_cad)
        print(paginacao)
        print(exs_giro)
        print(papel)
        print(disc_imp)
        print(refile_imp)
        print(desintercalacao)
        print(refile_acabamento)
        print(disc_acabamento)
        print(disc_manual)
        print('-'*20)

        
            
                            


