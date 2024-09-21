quant = int(input())
alunos = []

for i in range(quant):
    matricula = int(input())
    nome = input()
    codigo = input()
    nota1 = float(input())
    nota2 = float(input())

    aluno = {
        "matricula": matricula,
        "nome": nome,
        "codigo": codigo,
        "nota1": nota1,
        "nota2": nota2,
    }
    alunos.append(aluno)

for aluno in alunos:
    media = (aluno["nota1"] + (aluno["nota2"] * 2)) / 3
    aluno["media"] = media

    print(aluno)
