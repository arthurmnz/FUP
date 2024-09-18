matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        x = int(input())
        linha.append(x)
    matriz.append(linha)

soma = 0
for i in range(4):
    for j in range(i + 1, 4):
        soma += matriz[i][j]

print(soma)