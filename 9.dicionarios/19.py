pessoas = []
homens = []
mil_mais = []
maior_idade = 0
for i in range(5):
    endereco = {}
    cadastro = {}
    cadastro["nome"] = input("Nome: ")
    endereco["rua"] = input("Rua: ")
    endereco["bairro"] = input("Bairro: ")
    endereco["cidade"] = input("Cidade: ")
    endereco["estado"] = input("Estado: ")
    endereco["cep"] = input("CEP: ")
    cadastro["endereco"] = endereco
    cadastro["salario"] = float(input("Salario: "))
    cadastro["identidade"] = input("Identidade: ")
    cadastro["cpf"] = input("CPF: ")
    cadastro["civil"] = input("Estado Civil: ")
    cadastro["telefone"] = input("Telefone: ")
    cadastro["idade"] = int(input("Idade: "))
    cadastro["sexo"] = input("Sexo: ")
    if maior_idade < cadastro["idade"]:
        maior_idade = cadastro["idade"]
        indice = i
    if cadastro["sexo"] == "Masculino":
        homens.append(cadastro)
    if cadastro["salario"] > 1000:
        mil_mais.append(cadastro)
    pessoas.append(cadastro)
print("Pessoa com maior idade:")
print(pessoas[indice])
print("Pessoas do sexo masculino:")
for i in homens:
    print(i)
print("Pessoas com salario maior que 1000:")
for i in mil_mais:
    print(i)

entrada = input("Identidade: ")
for i in pessoas:
    if i["identidade"] == entrada:
        print(i)
