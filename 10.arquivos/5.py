text_name = input()
text_letter = input()
quant = 0

with open(text_name, "r") as arquivo:
    for linha in arquivo:
        for palavra in linha:
            if palavra == text_letter:
                quant += 1

print(quant)
