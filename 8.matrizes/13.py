matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        x = int(input())
        linha.append(x)
    matriz.append(linha)

somacolunas = [0] * 5

for j in range(5):
    soma = 0
    for i in range(5):
        soma += matriz[i][j]
        somacolunas[j] = soma

print(somacolunas)