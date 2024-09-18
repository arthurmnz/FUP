lista = []
for i in range(10):
    lista.append(int(input()))
    cont = 0
    if lista[i] > 0:
        for j in range(1, lista[i]+1):
            if lista[i] % j == 0:
                cont += 1
    else:
        for j in range(lista[i], 0):
            if lista[i] % j == 0:
                cont += 1
    if cont == 2:
        print(lista[i])
        print(i)
