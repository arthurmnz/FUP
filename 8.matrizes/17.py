matriz = []
matrizdividida = []

def primo(numero):
    if numero == 0:
        return False
    if numero == 2:
        return True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
        
    return True

for linha in range(12):
    matriz.append([])
    matrizdividida.append([])
    for coluna in range(13):
        numero = int(input(''))
        matriz[linha].append(numero)

for coluna in range(13):
    maiorprimo = float('-inf')
    menornumero = float('inf')
    for linha in range(12):
        if primo(abs(matriz[linha][coluna])) and matriz[linha][coluna] > maiorprimo:
            maiorprimo = matriz[linha][coluna]
        if matriz[linha][coluna] < menornumero:
            menornumero = matriz[linha][coluna]

    if maiorprimo != float('-inf'):
        divisor = maiorprimo
    else:
        divisor = menornumero
    
    for linha in range(12):
        matrizdividida[linha].append(matriz[linha][coluna] / divisor)

for item in matriz:
    for numero in item:
        print(f'{numero:.2f}', end=' ')
    print()

print()

for item in matrizdividida:
    for numero in item:
        print(f'{numero:.2f}', end=' ')
    print()
    
