def funcao(data):
    m = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    mes -= 1
    mes_extenso = m[mes]
    
    return f"{dia} de {mes_extenso} de {ano}"
