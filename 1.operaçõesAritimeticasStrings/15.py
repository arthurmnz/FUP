segundos = int(input())
hora = segundos // 3600
minutos = (segundos % 3600) // 60 
segundos2 = (segundos % 3600) % 60
print(f'{hora}\n{minutos}\n{segundos2}')