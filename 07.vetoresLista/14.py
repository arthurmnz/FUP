import random
lista = []
random.seed(int(input()))
count = 0
soma = 0
for i in range(12):
    lista.append(random.uniform(-10,10))
for n in lista:
    if n < 0:
        count += 1
    else:
        soma += n
print(count)
print(f"{soma:.2f}")

