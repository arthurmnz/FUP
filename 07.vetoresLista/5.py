numeros = []
numeros_quadrado = []
juntos = []
for i in range(10):
    n = float(input())
    numeros.append(n)
    numeros_quadrado.append(n**2)
juntos = numeros + numeros_quadrado
for i in juntos:
    print(f"{i:.2f}")