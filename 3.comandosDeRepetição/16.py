#S=1/n + proximo número impar/n+1 ... 99/50
nImpar=1
s=0
for i in range (1,51):
    s+=nImpar/i
    nImpar+=2
print(f"{s:.10f}")