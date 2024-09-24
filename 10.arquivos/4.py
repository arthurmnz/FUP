text_name = input()
quant_vogais = 0
quant_consoantes = 0

with open(text_name, "r") as arquivo:
    for linha in arquivo:
        for palavra in linha:
            if palavra.isalpha():
                if palavra.lower() in "aeiou":
                    quant_vogais += 1
                else:
                    quant_consoantes += 1

print(quant_vogais)
print(quant_consoantes)
