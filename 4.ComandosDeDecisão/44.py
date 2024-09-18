frase = str(input())
fraseInvertida = ''
for i in range(len(frase) -1,-1,-1):
    letra = frase[i]
    if letra == 'A':
        fraseInvertida += '*'
    elif letra == 'a':
        fraseInvertida += '*'
    else:
        fraseInvertida += letra
print(fraseInvertida)
