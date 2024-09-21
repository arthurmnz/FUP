def date(date1: dict, date2: dict) -> bool:
    if date1["ano"] < date2["ano"]:
        return True

    elif date1["ano"] == date2["ano"]:
        if date1["mes"] < date2["mes"]:
            return True

        elif date1["mes"] == date2["mes"]:
            if date1["dia"] < date2["dia"]:
                return True

    return False


def time(time1: dict, time2: dict) -> bool:
    if time1["hora"] < time2["hora"]:
        return True

    elif time1["hora"] == time2["hora"]:
        if time1["minuto"] < time2["minuto"]:
            return True

        elif time1["minuto"] == time2["minuto"]:
            if time1["segundo"] < time2["segundo"]:
                return True

    return False


quant = int(input())
dicionarios = []

for value in range(quant):
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))

    hora = int(input("Hora: "))
    minuto = int(input("Minuto: "))
    segundo = int(input("Segundo: "))

    descricao = input("Descricao: ")

    data = {"dia": dia, "mes": mes, "ano": ano}
    horario = {"hora": hora, "minuto": minuto, "segundo": segundo}

    dic = {"data": data, "horario": horario, "descricao": descricao}
    dicionarios.append(dic)

for i in range(len(dicionarios)):
    for j in range(i + 1, len(dicionarios)):
        if date(dicionarios[j]["data"], dicionarios[i]["data"]):
            dicionarios[i], dicionarios[j] = dicionarios[j], dicionarios[i]

        elif dicionarios[i]["data"] == dicionarios[j]["data"]:
            if time(dicionarios[j]["horario"], dicionarios[i]["horario"]):
                dicionarios[i], dicionarios[j] = dicionarios[j], dicionarios[i]

for i in range(len(dicionarios)):
    print(dicionarios[i])
