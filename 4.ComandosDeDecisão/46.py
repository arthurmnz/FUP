import re
frase = input().lower()
frase = re.sub(r"[^a-zA-Z]", " ", frase)
frase = frase.replace(" ", "")
tamanho = len(frase)
inverso = ""
for i in range(tamanho -1, -1, -1):
    inverso += frase[i]
if frase == inverso:
    print(True)
else:
    print(False)