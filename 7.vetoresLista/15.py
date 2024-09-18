lista = []
for i in range(10):
    lista.append(int(input()))

for i in range(10):
    for j in range(i + 1, len(lista)):
        if lista[i] == lista[j]:
            print(lista[i])
