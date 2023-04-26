def define_posicoes(linha,coluna,orientação,tamanho):
    posição = []
    i = 0 
    while i < tamanho:
        if orientação == 'vertical':
            posição.append([(linha+i),coluna])
        if orientação == 'horizontal':
            posição.append([linha,(coluna+i)])
        i += 1
    return posição

def preenche_frota(frota,nome_navio,linha,coluna,orientação,tamanho):
    novo_navio = {}
    if len(frota) > 0:
        p = 0
        lista = []
        for x in frota:
            if x == nome_navio:
                p = 1
                for x  in frota:
                    if x == nome_navio:
                        novo = define_posicoes(linha,coluna,orientação,tamanho)
                        for t in frota[x]:
                            antigo = t 
                            lista.append(antigo)
                        lista.append(novo)
                        novo_navio[nome_navio] = lista
    if len(frota) > 0 and p == 0 :
        novo = define_posicoes(linha,coluna,orientação,tamanho)
        novo_navio[nome_navio] = [novo]

    elif len(frota) == 0:
        novo = define_posicoes(linha,coluna,orientação,tamanho)
        novo_navio[nome_navio] = [novo]
        
    for y in frota:
        if y != nome_navio:
            novo_navio[y] = frota[y]
    return novo_navio
