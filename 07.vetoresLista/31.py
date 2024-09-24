def funcao(nome):
    letras_unicas = []
    
    for letra in nome:
        if letra.isalpha():
            if letra not in letras_unicas:
                letras_unicas.append(letra)
    
    print(len(letras_unicas))

