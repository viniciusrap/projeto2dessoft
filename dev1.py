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
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = [0]*10
    for i in range(len(tabuleiro)):
        tabuleiro[i] = [0]*10
    for x in frota:
        for y in frota[x]:
            for t in y:
                linha = t[0]
                coluna = t[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro
def afundados(frota,tabuleiro):
    soma = 0
    for x in frota:
        for y in frota[x]:
            test = 0
            for t in y:
                linha = t[0]
                coluna = t[1]
                if tabuleiro[linha][coluna] == 'X':
                    test += 1
            if test == len(y):
                soma += 1
    return soma
def posicao_valida(frota,linha,coluna,orientação,tamanho):
    posição = define_posicoes(linha,coluna,orientação,tamanho)
    for x in frota:
        for y in frota[x]:
            for t in y:
                for m in posição:
                    linha = m[0]
                    coluna = m[1]
                    if linha > 9 or coluna > 9 or linha < 0 or coluna <0:
                        return False
                    if t == m:
                        return False
    if len(frota) == 0:
        for m in posição:
                    linha = m[0]
                    coluna = m[1]
                    if linha > 9 or coluna > 9 or linha < 0 or coluna <0:
                        return False
    return True
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
tamanhodict = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1,
}
for x in frota:
    tamanho = tamanhodict[x]
    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(x,tamanho))

    linha = float(input('linha'))
    coluna = float(input('coluna'))
    orientação = ''
    if x != 'submarino':
        orienta = float(input('orientação'))
        if orienta == 1:
            orientação = 'vertical'
        elif orienta == 2:
            orientação = 'horizontal'
    verifica = posicao_valida(frota,linha,coluna,orientação,tamanho)
    c = True
    while c:
        if verifica == False:
            print('Esta posição não está válida!')
            linha = float(input('linha'))
            coluna = float(input('coluna'))
            orientação = ''
            if x != 'submarino':
                orienta = float(input('orientação'))
                if orienta == 1:
                    orientação = 'vertical'
                elif orienta == 2:
                    orientação = 'horizontal'
            verifica = posicao_valida(frota,linha,coluna,orientação,tamanho)
        if verifica == True:
            c = False
    frota = (preenche_frota(frota,x,linha,coluna,orientação,tamanho))
print(frota)

