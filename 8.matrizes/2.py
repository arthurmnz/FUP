n = int(input())
matrix = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matrix.append(linha)
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()
    