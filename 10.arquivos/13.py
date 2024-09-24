def ler_e_formatar_contatos(nome_arquivo):
    contatos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome, telefone = linha.strip().split('\t')
            contato = {'nome': nome, 'telefone': telefone}
            contatos.append(contato)
            lista_ordenada = sorted(contatos, key=lambda x: x["nome"])
    return lista_ordenada


def imprimir_contatos(lista_ordenada):
    for contato in lista_ordenada:
        print(contato)


nome_do_arquivo = input("")
contatos = ler_e_formatar_contatos(nome_do_arquivo)
imprimir_contatos(contatos)