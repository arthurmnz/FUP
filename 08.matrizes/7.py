matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        if i > j:
            formacao = 4 * (i**3) - 5 * (j**2) + 1

        elif i == j:
            formacao = 3 * (i**2) - 1
        elif i < j:
            formacao = (2*i) + (7*j) - 2
        linha.append(formacao)
    matriz.append(linha)

for linha in matriz:
    for i in linha:
        print(i, end = " ")
    print()