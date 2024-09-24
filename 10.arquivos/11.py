def funcao(file_name, word):
    contador = 0
    with open(file_name, "r") as file:
        for line in file:
            words = line.split()
            for current_word in words:
                if word.lower() in current_word.lower():
                    contador += 1
    return contador