#H(n)=1/1+1/2+1/3...1/n
def funcao(n):
    x=0
    for i in range(1,n+1):
        x+=1/i
    return x