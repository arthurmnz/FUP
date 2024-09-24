count = 0
matrix = [[],[],[],[]]
for i in range(4):
    for j in range(4):
        matrix[i].append(int(input()))
        if matrix[i][j] > 10:
            count += 1
print(count)