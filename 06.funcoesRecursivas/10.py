def funcao(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    return 2 * funcao(x-1) + 3 * funcao(x-2)