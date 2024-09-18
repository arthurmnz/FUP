palavra=input()
quantidade=len(palavra)
palavraInvertida=""
while quantidade:
    palavraInvertida+=palavra[quantidade-1]
    quantidade-=1
print(palavraInvertida)