lista = []
for valor in range(5):
    lista.append({})
    lista[valor]["modelo"] = input()
    lista[valor]["ano"] = int(input(""))
    lista[valor]["preco"] = float(input(""))

while True:
    preco_menor = int(input(""))

    if preco_menor == 0:
        break

    for i in range(len(lista)):
        if lista[i]["preco"] < preco_menor:
            print(lista[i])
