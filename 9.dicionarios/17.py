eletrodomesticos = []
consumo_total = 0

for value in range(5):
    eletrodomestico = {
        "nome": input(),
        "potencia": float(input()),
        "tempo": float(input()),
    }
    eletrodomesticos.append(eletrodomestico)

time = int(input())

for i in range(len(eletrodomesticos)):
    consumo = (eletrodomesticos[i]["potencia"] * eletrodomesticos[i]["tempo"]) * time
    eletrodomesticos[i]["consumo"] = consumo
    consumo_total += consumo

for i in range(len(eletrodomesticos)):
    consumo = (100 * eletrodomesticos[i]["consumo"]) / consumo_total
    eletrodomesticos[i]["consumo"] = consumo


print(f"{consumo_total:.2f}")
for i in range(len(eletrodomesticos)):
    print(f'{eletrodomesticos[i]["nome"]}: {eletrodomesticos[i]["consumo"]:.2f}')
