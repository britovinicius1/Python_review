####

#%%
#3) Crie um dicionario para armazenar infors de um livro
# incluindo titulo, autor e ano publicado. Imprima cada info

livro01: dict = {
    "titulo": "Game of thrones",
    "Autor": "Estagiario",
    "Ano": 2025
}

livro02: dict = {
    "titulo": "armas da persuação",
    "Autor": "John",
    "Ano": 2025
}

lista_de_livros = []
lista_de_livros.extend([livro01,livro02])
print(lista_de_livros)


# %%
##modelos mais usados tipo api
livros_completo = {
    "livro01": {
        "titulo": "Game of thrones",
        "Autor": "Estagiario",
        "Ano": 2025
    },
    "livro02": {
        "titulo": "armas da persuação",
        "Autor": "John",
        "Ano": 2025
    }  
}

print(livros_completo["livro01"]["titulo"])

# %%
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave in livro:
    print(f"{chave} -> {livro[chave]}")
# %%
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave} e {valor}")
# %%
#5) Preço total da lista de compras
lista_compras = ["maçã","maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total = 0

for item in lista_compras:
    total = precos[item] + total

print(total)

# %%
lista_compras = ["maçã","maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

valores = []

for item in lista_compras:
    valores.append(precos[item])
total = sum(valores)
print(total)

# %%
#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [22, 15, 30, 17, 18]

lista_maiores = []

for idade in idades:
    if idade >= 18:
        lista_maiores.append(idade)

print(lista_maiores)
        
# %%
