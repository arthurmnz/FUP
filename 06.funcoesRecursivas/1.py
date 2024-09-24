def funcao(x):
    if x == 0:
        return 0
    soma = x + funcao(x-1)
    return soma