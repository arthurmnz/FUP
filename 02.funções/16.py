def funcao(x):
    h=x//3600
    m=(x%3600)//60 
    s=(x%3600)%60
    return h,m,s