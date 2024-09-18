ve = int(input())
for i in range(ve):
    n = float(input())
    if i == 0:
        high = n
        low = n
    elif n > high:
        high = n
    elif n < low:
        low = n
print(f"{low:.2f}")
print(f"{high:.2f}")