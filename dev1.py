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
    if len(frota[x]) == 0:
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
quantidade = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4,
}
orientação =''
for x in frota:
    for l in range((quantidade[x])):
        tamanho = tamanhodict[x]
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(x,tamanho))

        linha = int(input('linha'))
        coluna = int(input('coluna'))
        if x != 'submarino':
            orienta = int(input('orientação'))
            if orienta == 1:
                orientação = 'vertical'
            elif orienta == 2:
                orientação = 'horizontal'
        verifica = posicao_valida(frota,linha,coluna,orientação,tamanho)
        c = True
        while c:
            if verifica == True:
                c = False
            if verifica == False:
                print('Esta posição não está válida!')
                print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(x,tamanho))
                linha = int(input('linha'))
                coluna = int(input('coluna'))
                if x != 'submarino':
                    orienta = int(input('orientação'))
                    if orienta == 1:
                        orientação = 'vertical'
                    elif orienta == 2:
                        orientação = 'horizontal'
                verifica = posicao_valida(frota,linha,coluna,orientação,tamanho)
        frota = (preenche_frota(frota,x,linha,coluna,orientação,tamanho))
             
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

posicoes_informadas = []
jogando = True
while jogando:

    linha = int(input('Informe a linha que deseja atacar (0-9): '))
    if linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Informe a linha que deseja atacar (0-9): '))
    
    coluna = int(input('Informe a coluna que deseja atacar (0-9): '))
    if coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Informe a coluna que deseja atacar (0-9): '))

    if [linha, coluna] in posicoes_informadas:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
    
    faz_jogada(linha, coluna,tabuleiro_oponente)
    posicoes_informadas.append([linha, coluna])

    if afundados(tabuleiro_jogador, tabuleiro_oponente) == 4:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
