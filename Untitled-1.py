def define_posicoes(linha,coluna,orientação,tamanho):
    posição = []
    i = 0 
    while i < len(tamanho):
        if orientação == 'vertical':
            posição.append([(linha+i),coluna])
        if orientação == 'horizontal':
            posição.append([linha,(coluna+i)])
        i += 1
    return posição



    



  
