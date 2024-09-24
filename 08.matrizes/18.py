import random

semente = int(input(''))
random.seed(semente)

matriz = []

triangular = []

for linha in range(5):
    matriz.append([])
    for coluna in range(5):
        matriz[linha].append(random.randint(1,20)) 

for linha in range(5):
    triangular.append([])
    for coluna in range(5):
        triangular[linha].append(matriz[linha][coluna] * (linha >= coluna))

for item in matriz:
    for numero in item:
        print(numero, end=' ')
    print()

print()

for item in triangular:
    for numero in item:
        print(numero, end=' ')
    print()

