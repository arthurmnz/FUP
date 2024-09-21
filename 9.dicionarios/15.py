livros = []

for value in range(5):
    livro = {"titulo": input(), "autor": input(), "ano": int(input())}
    livros.append(livro)

search_word = input()
for i in range(len(livros)):
    if str.lower(search_word) in str.lower(livros[i]["titulo"]):
        print(livros[i])
