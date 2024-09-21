quant = int(input())
alunos = []

for i in range(quant):
    nome = input()
    matricula = int(input())
    curso = input()

    aluno = {"nome": nome, "matricula": matricula, "curso": curso}
    alunos.append(aluno)

for aluno in alunos:
    print(aluno)
