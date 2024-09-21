alunos = dict()
maior_nota1 = 0
maior_media = 0
menor_media = float("inf")

aluno_media_maior = ""
aluno_media_menor = ""
aluno_maior_nota1 = ""
aluno_maior_nota_valor = 0

# Coleta dos dados de 5 alunos
for _ in range(5):
    matricula = int(input())
    nome = input()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media = (nota1 + nota2 + nota3) / 3

    # Armazena o aluno no dicionário com a matrícula como chave
    alunos[matricula] = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
    }

    # Verifica a maior nota entre todas as notas
    if nota1 > maior_nota1:
        maior_nota1 = nota1
        aluno_maior_nota1 = nome

    # Atualiza a maior média
    if media > maior_media:
        maior_media = media
        aluno_media_maior = nome

    # Atualiza a menor média
    if media < menor_media:
        menor_media = media
        aluno_media_menor = nome

# Exibição dos resultados após o laço
print(f"Aluno {aluno_maior_nota1} tem a maior nota1: {maior_nota1:.2f}")
print(f"Aluno {aluno_media_maior} tem a maior media: {maior_media:.2f}")
print(f"Aluno {aluno_media_menor} tem a menor media: {menor_media:.2f}")

# Exibe a situação de aprovação ou reprovação de cada aluno
for matricula, dados in alunos.items():
    if dados["media"] >= 7.00:
        status = "aprovado"
    else:
        status = "reprovado"
    print(f'Aluno {dados["nome"]} esta {status} com media {dados["media"]:.2f}')
