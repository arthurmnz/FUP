def funcao(lista01, lista02):
    nova = []
    for i in lista01:
        if i not in nova:
            nova.append(i)

    for i in lista02:
        if i not in nova:
            nova.append(i)

    return nova
