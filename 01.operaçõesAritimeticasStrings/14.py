numero = int(input())
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 1000) % 100 // 10
unidade = numero % 10
print(f'{milhar}\n{centena}\n{dezena}\n{unidade}')