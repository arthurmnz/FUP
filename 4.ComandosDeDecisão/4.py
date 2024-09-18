for i in range(3):
    n = float(input())
    if i == 0:
        high = n
    elif n > high:
        high = n
print(high)