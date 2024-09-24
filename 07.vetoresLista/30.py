def funcao(lista):
    max_size = len(lista)
    if max_size < 2:
        return -1, -1, -1

    max_tam = 0
    start_1 = -1
    start_2 = -1
    for i in range(2, max_size):
        for j in range(max_size - i + 1):
            segment_1 = lista[j:j+i]

            for k in range(j + 1, max_size - i + 1):
                segment_2 = lista[k:k + i]

                if segment_1 == segment_2 and i > max_tam:
                    max_tam = i
                    start_1 = j
                    start_2 = k
                    break

    if max_tam == 0:
        return -1, -1, -1
    else:
        return start_1, start_2, max_tam
