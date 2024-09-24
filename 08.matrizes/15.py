A = []
B = []
for i in range(5):
    linha = []
    for j in range(5):
        x = int(input())
        linha.append(x)
    A.append(linha)

for i in range(5):
    linha = []
    for j in range(5):
        x = int(input())
        linha.append(x)
    B.append(linha)

C = [[0 for _ in range(5)]for _ in range(5)]
for i in range(5):
    for j in range(5):
        C[i][j] = 0
        for l in range(5):
            C[i][j] += A[i][l] * B[l][j]

for linha in C:
    for i in linha:
        print(i, end = " ")
    print()