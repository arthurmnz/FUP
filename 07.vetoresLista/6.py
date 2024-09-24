lista = []
for i in range(8):
    n = float(input())
    lista.append(n)
x = int(input())
y = int(input())

print(f"{lista[x] + lista[y]:.2f}")