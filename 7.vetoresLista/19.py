def funcao(x1,x2):
    nova = []
    for i in range(10):
        if i % 2 == 0:
            nova.append(x1[0])
            del x1[0]
        else:
            nova.append(x2[0])
            del x2[0]
    return nova