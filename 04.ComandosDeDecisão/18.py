dia = 0
mes = 0
ano = 0

def funcao(x):

    if x[0] == '0':
        dia = x[1]
    else:
        dia = x[:2]
   
    if x[3:5] == '01':
        mes = 'janeiro'
    elif x[3:5] == '02':
        mes = 'fevereiro'
    elif x[3:5] == '03':
        mes = 'marco'
    elif x[3:5] == '04':
        mes = 'abril'
    elif x[3:5] == '05':
        mes = 'maio'
    elif x[3:5] == '06':
        mes = 'junho'
    elif x[3:5] == '07':
        mes = 'julho'
    elif x[3:5] == '08':
        mes = 'agosto'
    elif x[3:5] == '09':
        mes = 'setembro'
    elif x[3:5] == '10':
        mes = 'outubro'
    elif x[3:5] == '11':
        mes = 'novembro'
    elif x[3:5] == '12':
        mes = 'dezembro'

    ano = x[6:]

    resposta = f'{dia} de {mes} de {ano}'

    return resposta
