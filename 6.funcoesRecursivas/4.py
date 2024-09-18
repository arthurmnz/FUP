def funcao(x1,x2):
    if x2 == 0:
        return 1
    return x1 * funcao(x1,x2-1)