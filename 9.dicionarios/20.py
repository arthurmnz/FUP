def definir_pessoas(vetor):
    dicionario = {
        "nome": "",
        "email": "",
        "endereco": {
            "rua": "",
            "numero": 0,
            "complemento": "",
            "bairro": "",
            "cep": "",
            "cidade": "",
            "estado": "",
            "pais": "",
        },
        "telefone": {"ddd": 0, "numero": ""},
        "nascimento": {"dia": 0, "mes": 0, "ano": 0},
        "observacao": "",
    }
    dicionario["nome"] = input("Nome: ")
    dicionario["email"] = input("E-mail: ")
    dicionario["endereco"]["rua"] = input("Rua: ")
    dicionario["endereco"]["numero"] = int(input("Numero: "))
    dicionario["endereco"]["complemento"] = input("Complemento: ")
    dicionario["endereco"]["bairro"] = input("Bairro: ")
    dicionario["endereco"]["cep"] = input("CEP: ")
    dicionario["endereco"]["cidade"] = input("Cidade: ")
    dicionario["endereco"]["estado"] = input("Estado: ")
    dicionario["endereco"]["pais"] = input("Pais: ")
    dicionario["telefone"]["ddd"] = int(input("DDD: "))
    dicionario["telefone"]["numero"] = input("Telefone: ")
    dicionario["nascimento"]["dia"] = int(input("Dia do nascimento: "))
    dicionario["nascimento"]["mes"] = int(input("Mes do nascimento: "))
    dicionario["nascimento"]["ano"] = int(input("Ano do nascimento: "))
    dicionario["observacao"] = input("Observacao: ")
    vetor.append(dicionario)
    return vetor


def buscar_nome(nome):
    for dic in vet:
        tam_primeiro_nome = len(nome)
        if nome == dic["nome"][:tam_primeiro_nome]:
            return dic


def buscar_mes(mes):
    for dic in vet:
        if mes == dic["nascimento"]["mes"]:
            return dic


def buscar_mes_dia(dia, mes):
    for dic in vet:
        if mes == dic["nascimento"]["mes"] and dia == dic["nascimento"]["dia"]:
            return dic


vet = []
dicionario = {
    "nome": "",
    "email": "",
    "endereco": {
        "rua": "",
        "numero": 0,
        "complemento": "",
        "bairro": "",
        "cep": "",
        "cidade": "",
        "estado": "",
        "pais": "",
    },
    "telefone": {"ddd": 0, "numero": ""},
    "nascimento": {"dia": 0, "mes": 0, "ano": 0},
    "observacao": "",
}

while True:
    print(
        "1: Inserir uma pessoa\n"
        "2: Buscar por primeiro nome\n"
        "3: Buscar por mes de nascimento\n"
        "4: Buscar por dia e mes de nascimento\n"
        "5: Imprimir agenda\n"
        "0: Sair"
    )

    opcao = int(input("Opcao: "))
    if opcao == 0:
        break
    elif opcao == 1:
        resultado = definir_pessoas(vet)
    elif opcao == 2:
        nome = str(input("Primeiro nome: "))
        res_busca_nome = buscar_nome(nome)
        if res_busca_nome:
            print(res_busca_nome)
    elif opcao == 3:
        mes = int(input("Mes de nascimento: "))
        res_busca_mes = buscar_mes(mes)
        if res_busca_mes:
            print(res_busca_mes)
    elif opcao == 4:
        dia = int(input("Dia do nascimento: "))
        mes = int(input("Mes do nascimento: "))
        res_busca_mes_dia = buscar_mes_dia(dia, mes)
        if res_busca_mes_dia:
            print(res_busca_mes_dia)
    elif opcao == 5:
        print("1: Imprimir apenas nome, telefone e email")
        print("2: Imprimir todos os dados")
        opcao2 = int(input("Opcao: "))

        if opcao2 == 1:
            for dic in vet:
                reduced_dic = dict(
                    nome=dic["nome"], telefone=dic["telefone"], email=dic["email"]
                )
                print(reduced_dic)

        elif opcao2 == 2:
            for dic in vet:
                print(dic)

        else:
            print("Opcao invalida")
    else:
        print("Opcao invalida")
        continue
