def verification_date(date: str) -> bool:
    for i in range(len(date)):
        if i == 2 or i == 5:
            if date[i] != "/":
                return False

        else:
            if not date[i].isdigit():
                return False

    return True


def verification_cep(cep: str) -> bool:
    for i in range(len(cep)):
        if i == 2:
            if cep[i] != ".":
                return False

        elif i == 6:
            if cep[i] != "-":
                return False

        else:
            if not cep[i].isdigit():
                return False

    return True


def verification_email(email: str) -> bool:
    for i in range(len(email)):
        if "@" not in email:
            return False
        elif email.count("@") > 1:
            return False
        elif email[0] == "@" or email[-1] == "@":
            return False
        elif email[i] == "@" and not email[i + 1].isalpha():
            return False
        elif email.count(".") == 0:
            return False
    return True


usuario = {
    "nome": input(),
    "endereco": input(),
    "nascimento": input(),
    "cidade": input(),
    "cep": input(),
    "email": input(),
}

if not verification_date(usuario["nascimento"]):
    print("Data errada")

elif not verification_cep(usuario["cep"]):
    print("CEP errado")

elif not verification_email(usuario["email"]):
    print("E-mail errado")

else:
    print(usuario)
