def main():

    alunos = []

    while len(alunos) < 5:
        nome = input("Aluno: ")
        alunos.append(nome)

        if len(alunos) < 5:
            continuar = input("Deseja inserir novo aluno? [S/N]: ")
            if continuar.lower() != 's':
                break

    nome_pesquisar = input("Aluno para pesquisa: ")

    encontrado = False
    for i, aluno in enumerate(alunos):
        if nome_pesquisar.lower() in aluno.lower():
            print(f"{aluno}")
            print(f"{i}")
    

# Chama a função principal
main()
