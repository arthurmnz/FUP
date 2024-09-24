agendas = []
for value in range(5):
    agenda = {
        "compromisso": input("Descricao: "),
        "data": {
            "dia": int(input("Dia: ")),
            "mes": int(input("Mes: ")),
            "ano": int(input("Ano: ")),
        },
    }
    agendas.append(agenda)

while True:
    mes_data = int(input())
    if mes_data == 0:
        break

    ano_data = int(input())

    for i in range(len(agendas)):
        for j in range(i + 1, len(agendas)):
            if (
                agendas[i]["data"]["mes"] != mes_data
                or agendas[i]["data"]["ano"] != ano_data
            ):
                break

            dic1 = agendas[i]
            dic2 = agendas[j]

            if dic1["data"]["dia"] > dic2["data"]["dia"]:
                agendas[i], agendas[j] = agendas[j], agendas[i]

    for i in range(len(agendas)):
        if (
            agendas[i]["data"]["ano"] == ano_data
            and agendas[i]["data"]["mes"] == mes_data
        ):
            print(agendas[i])
