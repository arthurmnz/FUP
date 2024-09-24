import math


def soma(dic1: dict, dic2: dict) -> dict:
    soma_real = dic1["real"] + dic2["real"]
    soma_imaginaria = dic1["imaginario"] + dic2["imaginario"]
    return {"real": soma_real, "imaginario": soma_imaginaria}


def diff(dic1: dict, dic2: dict) -> dict:
    diff = dic1["real"] - dic2["real"]
    diff_imaginaria = dic1["imaginario"] - dic2["imaginario"]
    return {"real": diff, "imaginario": diff_imaginaria}


def product(dic1: dict, dic2: dict) -> dict:
    dic1_real = dic1["real"]
    dic1_imaginario = dic1["imaginario"]
    dic2_real = dic2["real"]
    dic2_imaginario = dic2["imaginario"]

    return {
        "real": (dic1_real * dic2_real) - (dic1_imaginario * dic2_imaginario),
        "imaginario": (dic1_real * dic2_imaginario) + (dic1_imaginario * dic2_real),
    }


def modulo(dic: dict):
    real = dic["real"]
    imaginario = dic["imaginario"]

    return math.sqrt(real**2 + imaginario**2)


numbers = []

for i in range(2):
    dicionario = {"real": float(input()), "imaginario": float(input())}
    numbers.append(dicionario)

dic1, dic2 = numbers

result_soma = soma(dic1, dic2)
result_diff = diff(dic1, dic2)
result_Product = product(dic1, dic2)
result1 = modulo(dic1)
result2 = modulo(dic2)

print(result_soma)
print(result_diff)
print(result_Product)
print(f"{result1:.2f}")
print(f"{result2:.2f}")
