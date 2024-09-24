def ehTriangulo(a,b,c):
    if a + b > c and b + c > a and a + c > b:   
        return True
    return False


def tipoTriangulo(a,b,c):
    if a == b and b == c:
        return 'Triangulo equilatero'
    if a != b and b != c and c != a:
        return 'Triangulo escaleno'
    return 'Triangulo isosceles'




a = int(input()) 
b = int(input())
c = int(input())


if ehTriangulo(a,b,c):
    print(tipoTriangulo(a,b,c))
else:
    print('Nao triangulo')