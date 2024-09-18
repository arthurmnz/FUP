matriz = []
soma = 0
for i in range(4):
    linha = []
    for j in range(4):
        x = int(input())
        linha.append(x)
        if i + j == 3:
            soma += x
    matriz.append(linha)

print(soma)