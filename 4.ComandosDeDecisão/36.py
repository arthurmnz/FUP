def funcao(x):
    fator = 2
    ultimo = 1
    
    for i in range(1, x):
        if x % fator == 0:
            ultimo = fator
            x //= fator
        
        else:
            fator += 1
    return ultimo
