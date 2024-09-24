cont = 0
s = 0
while True:
    if cont == 10:
        break
    n = int(input())
    if n > 0:
        cont += 1
        s += n
print(f"{s/10:.2f}")