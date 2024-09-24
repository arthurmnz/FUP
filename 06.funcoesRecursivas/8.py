def SomaSerie(x1,x2,x3):
    if x1 == x2:
        return x2
    if x1 > x2:
        return 0
    return x1 + SomaSerie(x1+x3,x2,x3)