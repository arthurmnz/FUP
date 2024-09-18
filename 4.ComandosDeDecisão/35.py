for i in range(1000 , 10000):
    resto = i % 100 
    divisor = i // 100

    soma = resto + divisor
    
    if (soma ** 2 == i):
        print(i)


