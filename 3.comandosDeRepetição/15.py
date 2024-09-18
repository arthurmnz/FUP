from math import factorial
def funcao(n):
    x=0
    for i in range (0,n+1):
        x=x+1/factorial(i)
    return x