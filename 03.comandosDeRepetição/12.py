#n!/(k!*(n-k)!)
def funcao(x1,x2):
    x3=x1-x2
    x1fat=1
    x2fat=1
    x3fat=1
    for i in range(x1,0,-1):
            x1fat*=i
    for i in range(x2,0,-1):
            x2fat*=i
    for i in range(x3,0,-1):
            x3fat*=i  
    answer=x1fat/(x2fat*x3fat)
    return answer