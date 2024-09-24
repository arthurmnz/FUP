def funcao(lista01, lista02):
    nova = []
    for i in lista01:
        for j in lista02:
            if i == j and i not in nova:
                nova.append(i)
    return nova
