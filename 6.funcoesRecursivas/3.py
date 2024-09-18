def funcao(x):
    if x == 1:
        return 1
    return x ** 3 + funcao(x-1) 