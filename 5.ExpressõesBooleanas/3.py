frase = str(input())
letra = str(input())
fraseNova = ''
quantidade = 0
for i in frase:
    if i in "aeiouAEIOU":
        quantidade +=1
        fraseNova += letra
    else:
        fraseNova += i
print(quantidade)
print(fraseNova)