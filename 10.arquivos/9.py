arquivo_1 = input("")
arquivo_2 = input("")
arquivo_3 = f"{arquivo_1}{arquivo_2}"

vet = []

with open(arquivo_1, "r") as primeiro:
    for linha in primeiro:
        vet.append(linha)
with open(arquivo_2, "r") as segundo:
    for linha in segundo:
        vet.append(linha)

with open(arquivo_3, "w") as terceiro:
    for i in vet:
        terceiro.write(i)

with open(arquivo_3, "r") as arquivo_final:
    for item in arquivo_final:
        print(item, end="")
    print()
