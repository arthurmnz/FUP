lista = []
while len(lista) < 12:
    num = int(input())
    if num not in lista:
        lista.append(num)
    else:
        print(f"Numero {num} ja existe, escreva outro")
print(lista)
