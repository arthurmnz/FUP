from math import factorial

def funcao(P):
    fatorial = factorial(P)
    soma = 0
    while fatorial:
        soma += fatorial % 10
        fatorial //= 10  
    return soma