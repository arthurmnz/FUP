n1 = float(input())
n2 = float(input())
n3 = float(input())
if n3 == 1:
    print(f'{(n1 + n2) / 2:.2f}')
elif n3 == 2:
    if n1 > n2:
        print(f'{n1 - n2:.2f}')
    else:
        print(f'{n2 - n1:.2f}')
elif n3 == 3:
    print(f'{n1 * n2:.2f}')
elif n3 == 4:
    if n2 == 0:
        print('Erro')
    else:    
        print(f'{n1 / n2:.2f}')
else:
    print('Erro')