dic = {}

for value in range(5):
    model = input()
    litros = float(input())
    dic[model] = litros

menorconsumidor = [0, 0]

for key, value in dic.items():
    if value > menorconsumidor[1]:
        menorconsumidor = [key, value]

print(f"Carro mais economico: {menorconsumidor[0]}")

for key, value in dic.items():
    distance = value * 50
    print(f"Carro {key} percorre {distance:.2f} kms com 50 litros")


for key, value in dic.items():
    distance = 1000 / value
    print(f"Carro {key} precisa de {distance:.2f} litros para percorrer 1000 kms")
