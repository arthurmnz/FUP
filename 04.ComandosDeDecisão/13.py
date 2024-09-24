a = float(input())
b = float(input())
c = float(input())
if a == 0:
    print("Nao eh equacao do 2o grau")
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        print(f"{(-b + delta ** 0.5) / (2 * a):.2f}")
        print(f"{(-b - delta ** 0.5) / (2 * a):.2f}")
    elif delta == 0:
        print(f"{(-b + delta ** 0.5) / (2 * a):.2f}")
        print("Raiz unica")
    else:
        print("Nao existe raiz real")