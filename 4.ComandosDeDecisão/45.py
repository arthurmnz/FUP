def funcao(x1,x2):
    r = ""

    for letra in x1:
        if letra.isalpha():  
            if letra.isupper():
                a = ord('A')
            else:
                a = ord('a')
            n_posicao = (ord(letra) - a + x2) % 26
            if n_posicao >= 0:
                if n_posicao < 26:
                    r += chr(a + n_posicao)
        else:
            r += letra
    
    return r
