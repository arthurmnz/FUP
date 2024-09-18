while True:
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Saida")
    resp = int(input())
    
    if resp == 1:
        n1 = float(input())
        n2 = float(input())
        print(f"{n1+n2:.2f}")
    elif resp == 2:
        n1 = float(input())
        n2 = float(input())
        print(f"{n1-n2:.2f}")
    elif resp == 3:
        n1 = float(input())
        n2 = float(input())
        print(f"{n1*n2:.2f}")
    elif resp == 4:
        n1 = float(input())
        n2 = float(input())
        print(f"{n1/n2:.2f}")
    elif resp == 5:
        break
