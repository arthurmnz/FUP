def ehAposentado(idade,tempo):
    if idade >= 65:
        return True
    if tempo >= 30:
        return True
    if tempo >= 25 and idade >= 60:
        return True
    return False


idade = int(input())
tempo = int(input())

if ehAposentado(idade,tempo):
    print('Pode se aposentar')
else:
    print('Nao pode se aposentar')