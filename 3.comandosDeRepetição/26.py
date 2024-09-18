#sin(x) = (-1)n (x2n+1)/(2n+1)!
from math import factorial
def funcao(x1,x2):
    result=0
    for i in range (x2+1):
        result+=((-1)**i)*(x1**(2*i+1))/(factorial(2*i+1))
    return result
       