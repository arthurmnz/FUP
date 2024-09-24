def funcao(lista01, lista02):
    lista03 = []
    index = 0
    while len(lista03) < 5:
        lista03.append(lista01[index] - lista02[index])
        index += 1
    return lista03
