letra = str(input())
count = 0

for i in range(len(letra)):
    if( letra[i] == " "):
        count += 1
        
print(count)
