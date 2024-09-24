x = int(input())
count = 0
countN = 1

while count < x:
    n = int(input())
    
    if count == 0:
        high = n
        
    
    elif(n > high):
        high = n
        countN = 1
        
    elif (n == high):
        countN +=1
    count += 1

print(high)
print(countN)
