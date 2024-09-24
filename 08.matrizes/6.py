A = []
B = []

for i in range(4):
    linha = []
    for j in range(4):
        x = int(input())
        linha.append(x)
    A.append(linha)

for i in range(4):
    linha = []
    for j in range(4):
        x = int(input())
        linha.append(x)
    B.append(linha)

maiores = []
for i in range(4):
    linha = []
    for j in range(4):
        if A[i][j] > B[i][j]:
            maior = A[i][j]
        else:
            maior = B[i][j]
        linha.append(maior)
    maiores.append(linha)

for linha in maiores:
    for i in linha:
        print(i, end = " ")
    print()