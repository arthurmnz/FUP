empregado = []

for value in range(5):
    dic = {"nome": input(), "endereco": input(), "telefone": input()}
    empregado.append(dic)

for i in range(len(empregado)):
    for j in range(i + 1, len(empregado)):
        if empregado[i]["nome"] > empregado[j]["nome"]:
            empregado[i], empregado[j] = empregado[j], empregado[i]

for value in range(len(empregado)):
    print(empregado[value])
