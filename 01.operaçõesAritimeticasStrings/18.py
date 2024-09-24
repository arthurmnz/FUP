saque = int(input())
n100 = saque // 100
n50 = saque % 100 // 50
n20 = saque % 100 % 50 // 20
n10 = saque % 100 % 50 % 20 // 10
n5 = saque % 100 % 50 % 20 % 10 // 5
n2 = saque % 100 % 50 % 20 % 10 % 5 // 2
n1 = saque % 100 % 50 % 20 % 10 % 5 % 2 // 1
print(f'{n100}\n{n50}\n{n20}\n{n10}\n{n5}\n{n2}\n{n1}')