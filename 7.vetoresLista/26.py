def funcao(lista01, lista02):
    nova = []
    for i in range(5):
        if lista01[i] not in lista02 and lista01[i] not in nova:
            nova.append(lista01[i])
    return nova
