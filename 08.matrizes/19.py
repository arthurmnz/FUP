import random

linhas = int(input(''))
colunas = int(input(''))
semente = int(input(''))
comeco = int(input('')) 
fim = int(input(''))

random.seed(semente)
matriz = []

for linha in range(linhas):
    matriz.append([])
    for coluna in range(colunas):
        matriz[linha].append(random.randint(comeco, fim))

for item in matriz:
    for numero in item:
        print(numero, end=' ')
    print()

for linha in range(linhas):
    soma_pares = []
    quantidade_numeros_negativos_divisiveis_por_3 = 0
    for coluna in range(colunas):
        total_pares = 0
        if linha % 2 == 0:
            soma_pares.append(matriz[linha][coluna])
            for item in soma_pares:
                total_pares += item
            media_elementos_linhas_pares = total_pares/len(soma_pares)

        if linha % 2 != 0 and matriz[linha][coluna] % 3 == 0 and matriz[linha][coluna] < 0:
            quantidade_numeros_negativos_divisiveis_por_3 += 1

    if linha % 2 == 0:
        print(f'{media_elementos_linhas_pares:.2f}')
    else: 
        print(f'{quantidade_numeros_negativos_divisiveis_por_3}')
