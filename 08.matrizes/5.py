matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        numero = int(input())
        linha.append(numero)
    matriz.append(linha)

n = int(input())
found = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == n:
            print(i)
            print(j)
            found = True
            break
    if found:
        break
if not found:
    print('Nao encontrado')