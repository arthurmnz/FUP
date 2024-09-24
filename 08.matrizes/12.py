matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        x = int(input())
        linha.append(x)
    matriz.append(linha)

transposta = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        transposta[j][i] = matriz[i][j]

for linha in transposta:
    for i in linha:
        print(i, end = " ")
    print()