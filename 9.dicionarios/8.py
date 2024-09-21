import math

r = float(input())
a = float(input())

conjuntos = {"r": r, "a": a}
print(conjuntos)

x = r * math.cos(a)
y = r * math.sin(a)

cartesiano = {"x": x, "y": y}
print(cartesiano)
