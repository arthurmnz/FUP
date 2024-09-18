n = int(input())
matrix = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(i*j)
    matrix.append(linha)
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()