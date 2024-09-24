def ehBissexto(ano):
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        return True
    return False


ano = int(input())

if ehBissexto(ano):
    print('Bissexto')
else:
    print('Nao bissexto')