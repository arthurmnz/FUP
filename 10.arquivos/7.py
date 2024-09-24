arquivo = input("")
novo_arquivo = f"{arquivo}.out"
novo_texto = []
vogais = "aeiouAEIOU"
with open(arquivo, "r") as arquivo:
    for linha in arquivo:
        novo_texto.append("")
        for caractere in linha:
            cont = 0
            if caractere in vogais:
                novo_texto[cont] += "*"
                cont += 1
            else:
                novo_texto[cont] += caractere
                cont += 1

with open(novo_arquivo, "w") as arquivo_saida:
    for i in range(len(novo_texto)):
        arquivo_saida.write(novo_texto[i])

with open(novo_arquivo, "r") as arquivo_final:
    for item in arquivo_final:
        print(item, end="")
    print()
