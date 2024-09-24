arquivo = input("")
novo_arquivo = f"{arquivo}.out"
novo_texto = []
with open(arquivo, "r") as arquivo1:
    for linha in arquivo1:
        novo_texto.append("")
        for caractere in linha:
            i = 0
            novo_texto[i] += caractere.upper()
            i += 1
            
with open(novo_arquivo, "w") as arquivo_saida:
    for i in range(len(novo_texto)):
        arquivo_saida.write(novo_texto[i])

with open(arquivo, "r") as arquivo_fim:
    for item in arquivo_fim:
        print(item, end="")
    
with open(novo_arquivo, "r") as arquivo_final:
    for item in arquivo_final:
        print(item, end="")
    print()
