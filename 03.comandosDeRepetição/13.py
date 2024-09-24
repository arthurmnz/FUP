#F0=0() f1=1() f2=1(f0+f1) f3=2(f1+f2) f4=3(f3+f2) f5=5(f4+f3) f6=8(f5+f4) f7=13(f6+f5) ...
def funcao (n):
    f1 = 0
    f2 = 1
    fn = 1
    for i in range(2,n + 1):
        fn = f1 + f2
        f1 = f2    
        f2 = fn
    return fn