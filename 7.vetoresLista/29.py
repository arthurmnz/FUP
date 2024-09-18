def funcao(lista):
    auxilio = []
    for i in range(len(lista)):
        auxilio.append(lista[i])

    maior = []

    while len(auxilio) > 0:
        n_maior = auxilio[0]
        for i in range(len(auxilio)):
            if auxilio[i] > n_maior:
                n_maior = auxilio[i]
        maior.append(n_maior)
        auxilio.remove(n_maior)

    return maior
