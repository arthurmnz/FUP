def funcao(lista, x):
    nova = []
    for i in lista:
        if i % x == 0:
            nova.append(i)
    return nova
