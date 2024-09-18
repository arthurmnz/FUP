n = 1
parada = 0
lista = []

while parada == 0:
    if n % 7 != 0 and n % 10 != 7:
        lista.append(n)
    if len(lista) == 100:
        parada = 1
    n += 1
print(lista)
