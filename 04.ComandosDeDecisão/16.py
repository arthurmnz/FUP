maior = 1
menor = 1
cont = 0
while True:  
    num = int(input())
    if num >= 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        cont += 1
    else:
        break
if cont >= 2:
    print(f"{maior} \n{menor}")
elif cont == 1:
    print(f"{maior} \n{maior}")
else:
    print()