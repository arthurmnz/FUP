estoque = []

for i in range(5):
    estoque.append(
        {
            "codigo": int(input()),
            "nome": input(),
            "preco": float(input()),
            "quantidade": int(input()),
        }
    )

while True:
    produto_encontrado = False
    produto_suficiente = False
    for i in estoque:
        print(i)
    codigo_pedido = int(input())

    if codigo_pedido == 0:
        break

    quantidade_pedido = int(input())

    for i in estoque:
        if codigo_pedido == i["codigo"]:
            produto_encontrado = True
            produto = i
            if produto["quantidade"] >= quantidade_pedido:
                produto["quantidade"] -= quantidade_pedido
                produto_suficiente = True
    if produto_encontrado:
        if produto_suficiente:
            continue
        else:
            print("Impossivel atender ao pedido, produto sem estoque suficiente")
    else:
        print("Impossivel atender ao pedido, codigo nao encontrado")
