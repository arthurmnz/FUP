num_caracteres = 0
num_linhas = 0
num_palavras = 0
frequencia_letras = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}

nome_arquivo = input()

with open(nome_arquivo,'r') as arquivo:
    for linha in arquivo:
        num_linhas += 1
        num_caracteres += len(linha)
        
        palavras = linha.split()
        num_palavras += len(palavras)
        
        for letra in linha.lower():
            if 'a' <= letra <= 'z':
                frequencia_letras[letra] += 1


print(num_caracteres)
print(num_linhas)
print(num_palavras)
for letra in sorted(frequencia_letras.keys()):
    print(f"{letra}: {frequencia_letras[letra]}")
