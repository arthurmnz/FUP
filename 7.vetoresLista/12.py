def funcao(lista):
    somatorio = 0
    for i in lista:
        somatorio += (i - sum(lista)/15) ** 2  
    dp =(somatorio / len(lista)) ** 0.5
    return sum(lista)/15, dp