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


def desperdicio_acbto_interno(disc_acab, refile_acab):
    pass


