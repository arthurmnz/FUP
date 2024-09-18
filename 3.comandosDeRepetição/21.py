def funcao(x):
    for i in range(1, x + 1):
            for j in range(x - i):
                print(" ", end="")
            for j in range(2 * i - 1):
                print("*", end="")
            print()