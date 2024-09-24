nomeNovo = ""
idadeNova = None
nomeVelho = ""
idadeVelho = None   
while True:
    nome = str(input())
    idade = int(input())
    if idade < 0:
        break
    if idadeNova == None:
        idadeNova = idade
        nomeNovo = nome
        idadeVelho = idade
        nomeVelho = nome
    else:
        if idade < idadeNova:
            idadeNova = idade
            nomeNovo = nome
        if idade > idadeVelho:
            idadeVelho = idade
            nomeVelho = nome
            
print(nomeNovo)
print(idadeNova)
print(nomeVelho)
print(idadeVelho)
