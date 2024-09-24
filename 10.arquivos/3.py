filename = input()

with open(filename, "r") as file:
    vowels = 0
    for char in file.read():
        if char.lower() in "aeiou":
            vowels += 1
    print(vowels)
