lista = []
for i in range(20):
    n = int(input())
    if n < 0:
        lista.append(0)
    else:
        lista.append(n)
for i in lista:
    print(i)