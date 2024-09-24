filename = input()

with open(filename, "r") as file:
    print(len(file.readlines()))
