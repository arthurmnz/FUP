alunos = []
for value in range(10):
    aluno = {"nome": input(), "matricula": int(input()), "media": float(input())}
    alunos.append(aluno)

alunos_aprovados = []
alunos_reprovados = []

for aluno in alunos:
    if aluno["media"] >= 5:
        alunos_aprovados.append(aluno)
    else:
        alunos_reprovados.append(aluno)

for aluno in alunos_aprovados:
    print(aluno)

for aluno in alunos_reprovados:
    print(aluno)
