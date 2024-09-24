def simplificar(x1, x2):
    if x2 > x1:
        for i in range(1,x2):
            if x1 % i == 0:
                if x2 % i == 0:
                    x1 = (x1/i)
                    x2 = (x2/i)
    elif x1 > x2:
        for i in range(1, x1):
            if x1 % i == 0:
                if x2 % i == 0:
                    x1 = (x1/i)
                    x2 = (x2/i)
    elif x1 == x2:
        x1 = 1
        x2 = 1
    if x1 % 2 == 0:
        if x2 % 2 == 0:
            x1 = (x1/2)
            x2 = (x2/2)
    x1 = int(x1)
    x2 = int(x2)
    return x1, x2
