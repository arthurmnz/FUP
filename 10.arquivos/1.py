with open("arq.txt", "a") as file:
    while True:
        text = input("")

        if text == "0":
            break

        file.write(text + "\n")


with open("arq.txt", "r") as file:
    for line in file.readlines():
        print(line, end="")
