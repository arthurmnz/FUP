bi = str(input())
zero = '0'
um = '1'
quantidade0 = len(zero)
frase = ""

i = 0
while i < len(bi):
    if bi[i:i + quantidade0] == zero:
        frase += um
        i += quantidade0
    else:
        frase += bi[i]
        i += 1
print(frase)
