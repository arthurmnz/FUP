A = []
B = []

for i in range(4):
    linha = []
    for j in range(5):
        x = int(input())
        linha.append(x)
    A.append(linha)

for i in range(4):
    linha = []
    for j in range(5):
        x = int(input())
        linha.append(x)
    B.append(linha)

C = []
for i in range(4):
    linha = []
    for j in range(5):
        soma = A[i][j] + B[i][j]
        linha.append(soma)
    C.append(linha)

for linha in C:
    for i in linha:
        print(i, end = " ")
    print()