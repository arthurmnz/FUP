def mdc(x1, x2):
    
    if (x2 == 0):
        return x1
    
    resto = x1 % x2
    x1 = x2
    x2 = resto
    return mdc(x1 ,x2)

