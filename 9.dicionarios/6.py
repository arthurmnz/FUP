vect1 = []
for i in range(3):
    vect1.append(float(input()))

vect2 = []
for i in range(3):
    vect2.append(float(input()))

dict = {"x": vect1[0] + vect2[0], "y": vect1[1] + vect2[1], "z": vect1[2] + vect2[2]}

print(dict)
