n1 = int(input())
n2 = int(input())

if n1 > n2:
    divisor = (n1 * (n2 ** -1))
else:
    divisor = (n2 * (n1 ** -1))
print(f"{divisor:.0f}")
