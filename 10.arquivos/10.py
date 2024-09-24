def ler_cidades(arquivo_entrada):
    cidades = []
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        for linha in file:
            nome, habitantes = linha.strip().split('\t')
            cidades.append({'nome': nome, 'habitantes': int(habitantes)})
    return cidades

def encontrar_cidade_mais_populosa(cidades):
    return max(cidades, key=lambda cidade: cidade['habitantes'])

def escrever_saida(arquivo_saida, cidade_populosa):
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        file.write(f"{cidade_populosa['nome']}\t{cidade_populosa['habitantes']}\n")

def main():
    arquivo_entrada = input()
    arquivo_saida = input()
    cidades = ler_cidades(arquivo_entrada)
    cidade_populosa = encontrar_cidade_mais_populosa(cidades)
    escrever_saida(arquivo_saida, cidade_populosa)
    
    for cidade in cidades:
        print(cidade)
    
    print(f"{cidade_populosa['nome']}\t{cidade_populosa['habitantes']}")

if __name__ == "__main__":
    main()