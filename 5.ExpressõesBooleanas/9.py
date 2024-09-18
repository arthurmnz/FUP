def funcao(x1, x2):
    acumulador = 0

    if x1 > x2:
        maior = x1
    else:
        maior = x2

    while True:
        if (maior % x1 == 0) and (maior % x2 == 0):
            acumulador *= maior
            break
        else:
            maior += 1

    return maior