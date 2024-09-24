matriz = []

for linha in range(20):
    matriz.append([])
    for coluna in range(20):
        matriz[linha].append(int(input()))
    
maior_numero = float('-inf')

for linha in range(20):
    for coluna in range(17):
        numero = matriz[coluna - 1][linha] * matriz[coluna][linha] * matriz[coluna + 1][linha] * matriz[coluna + 2][linha]
        if numero > maior_numero:
            maior_numero = numero
            coordenada_x = coluna - 1
            coordenada_y = linha
            local = 'baixo'
        numero_2 = matriz[linha][coluna - 1] * matriz[linha][coluna] * matriz[linha][coluna + 1] * matriz[linha][coluna + 2]
        if numero_2 > maior_numero:
            maior_numero = numero_2
            coordenada_x = linha
            coordenada_y = coluna - 1
            local = 'direita'

for linha in range(17):
    for coluna in range(17):
        numero = matriz[linha - 1][coluna - 1] * matriz[linha][coluna] * matriz[linha + 1][coluna + 1] * matriz[linha + 2][coluna + 2]
        if numero > maior_numero:
            maior_numero = numero
            coordenada_x = linha - 1
            coordenada_y = coluna - 1
            local = 'direita baixo'

for linha in range(17):
    for coluna in range(3, 20):
        numero = matriz[linha][coluna] * matriz[linha + 1][coluna - 1] * matriz[linha + 2][coluna - 2] * matriz[linha + 3][coluna - 3]
        if numero > maior_numero:
            maior_numero = numero
            coordenada_x = linha
            coordenada_y = coluna
            local = 'esquerda baixo'

print(f'{maior_numero}')
print(f'{coordenada_x}')
print(f'{coordenada_y}')
print(f'{local}')