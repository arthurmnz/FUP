lista = []
impares = []
for i in range(15):
    n = int(input())
    lista.append(n)
for j in lista:
    if j % 2 != 0:
        impares.append(j)
print(sum(impares))
for k in impares:
    print(k)