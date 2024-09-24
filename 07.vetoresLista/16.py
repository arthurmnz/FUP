def funcao(lista):
    nova = []

    for i in range(len(lista)):
        cond = False
    
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                cond = True
                break
    
    
        if cond == False:
            nova.append(lista[i])
    return nova