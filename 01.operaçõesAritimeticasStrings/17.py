amigo1 = float(input())
amigo2 = float(input())
amigo3 = float(input())
premio = float(input())
total = amigo1 + amigo2 + amigo3
ganho1 = (amigo1 / total) * premio
ganho2 = (amigo2 / total) * premio 
ganho3 = (amigo3 / total) * premio  
print(f'{ganho1:.2f}\n{ganho2:.2f}\n{ganho3:.2f}')