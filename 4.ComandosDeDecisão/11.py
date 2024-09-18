n1 = float(input())
op = str(input())
n2 = float(input())
if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(f'{n1*n2:.2f}')
elif op == '/':
    print(f'{n1/n2:.2f}')
    