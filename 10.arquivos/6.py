text_name = input()

letters = {}

for letra in "abcdefghijklmnopqrstuvwxyz":
    letters[letra] = 0

with open(text_name, "r") as arquivo:
    for palavra in arquivo:
        for letra in palavra:
            if letra.isalpha():
                letters[letra.lower()] += 1

for letra, number in letters.items():
    print(f"{letra}: {number}")
