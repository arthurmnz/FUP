lista = []
cond = 1
for i in range(100):
    lista.append(float(input()))

while cond != 0:
    cond = int(input())
    if cond == 1:
        for i in range(len(lista)):
            print(f"{lista[i]:.1f}")
    elif cond == 2:
        for i in range(99, -1, -1):
            print(f"{lista[i]:.1f}")
    elif cond != 0:
        print("Codigo invalido")
