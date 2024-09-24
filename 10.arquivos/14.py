def calcular_idade(data_nascimento, data_atual):
    dia_nasc, mes_nasc, ano_nasc = data_nascimento
    dia_atual, mes_atual, ano_atual = data_atual
    idade = ano_atual - ano_nasc
    if mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc > dia_atual):
        idade -= 1
    return idade

def ler_e_processar_arquivo(nome_arquivo, data_atual):
    cadastros = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            nome, data_nascimento_str = linha.strip().split('\t')
            dia_nasc, mes_nasc, ano_nasc = map(int, data_nascimento_str.split())
            idade = calcular_idade([dia_nasc, mes_nasc, ano_nasc], data_atual)
            cadastros.append((nome, idade))

    nome_saida = nome_arquivo + ".out"
    with open(nome_saida, "w") as arquivo_saida:
        for nome, idade in cadastros:
            arquivo_saida.write(f"{nome}\t{idade}\n")

    with open(nome_saida, "r") as arquivo_saida:
        print(arquivo_saida.read())

nome_arquivo = input("")
dia_atual = int(input(""))
mes_atual = int(input(""))
ano_atual = int(input(""))
data_atual = [dia_atual, mes_atual, ano_atual]

ler_e_processar_arquivo(nome_arquivo, data_atual)