soma = 0
multi = 1
count = 2

while count:
    number = int(input())
    if count == 2:
        high = number
        low = number
        
    elif number > high:
        high = number
        
    elif number < low:
        low = number

    count -=1

for i in range(low,high + 1):
    
    if(i % 2 == 0):
        soma += i
    
    else:
        multi *= i

print(soma)
print(multi)
