s = 0
for i in range(3):
    x = float(input())
    if x >= 0:
        if x <= 10:
            s += x
            if i == 2:
                media=s/3
                print(f"{media:.2f}")
        else:
            print("Nota invalida")
            break
    else:
        print("Nota invalida")
        break