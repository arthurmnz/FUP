matriz = []
matrizdividida = []
for i in range(12):
    matrizdividida.append([])
    linha = []
    for n in range(13):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

modulomax = []
for i in range(12):
    maior = 0
    for j in range(13):
        if abs(matriz[i][j]) > maior:
            maior = abs(matriz[i][j])
    modulomax.append(maior)

for i in range(12):
    for j in range(13):
        matrizdividida[i].append(matriz[i][j] / modulomax[i])
        
for linha in matriz:
    for i in linha:
        print(f'{i:.2f}', end = " ")
    print()

print()

for i in matrizdividida:
    for j in i:
        print(f'{j:.2f}', end = " ")
    print()