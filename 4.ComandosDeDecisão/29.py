n = int(input())
cont = 0
for i in range(1,n):
    if n % i == 0:
        cont += 1
if cont == 1:
    print("Primo")
else:
    print("Nao primo")