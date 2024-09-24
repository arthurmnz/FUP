from math import inf
matrix = []
maior = -float('inf')
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
        if linha[j] > maior:
            maior = linha[j]
            row = i
            colomn = j
    matrix.append(linha)
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()
print(row)
print(colomn)
print(maior)