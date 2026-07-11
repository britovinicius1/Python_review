#trazendo mais alguns conteudos de dicionarios
# Dicionarios são pares chave valor
#%%
dados_vini = {
    "nome": "Vinicius",
    "idade": 30,
    "salario": 15000,
    "filhos": False,
    "formacao": ["Engenharia Quimica", "Data Science"],
    "cargos": [
        {"nome": "Estagiario", "empresa": "J&J"},
        {"nome": "Junior", "empresa": "Kenvue"}
    ]
}

# %%
print(dados_vini["cargos"][-1]["empresa"])
# %%
dados_vini["estado civil"] = "Solteiro"
#%%
print(dados_vini)
# %%
#retornando a lista de chaves e valores do dicionario
dados_vini.keys()
dados_vini.values()
# %%
#traz um lista com o par chave e valor
dados_vini.items()
# %%
#unpack ->
for i,j in dados_vini.items():
    print(f"{i} -> {j}")
# %%
#Escreva um programa que crie um dicionarioa com nomes
#de frutas como chaves e seus respectivos preços como valores. Solicite
#ao usuário o nome de uma frutra e exiba o preço correspondente.

fruta = input("Entre com o nome da fruta:")

frutas = {
    "Maça": "R$:2,50",
    "Pera": "R$:4,50",
    "Banana": "R$:6,50",
    "Uva": "R$:1,50"
}

if fruta in frutas: 
    print(frutas[fruta])
else:
    print("Entre com um valor valido...")
# %%
## Escreva um programa que solicite o usuario frases. Para parar de solicitar
#Frases ele pode apenas apertar "enter";
#Seu pgorama deve apresentar cada frase e quantas vezes ele fode escrita

frases = {}

while True:
    frase = input("Entre com uma frase: ")
    if frase == "":
        break
    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1

items = list(frases.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i,j in frases.items():
    print(f"A frase {i} apareceu -> {j} vezes")





# %%
#ordenando os valores, o dicionario não garente a ordem
dados = {
    "oi": 1,
    "ola": 3,
    "oi tudo bem": 40,
    "teste": 6
}

items.sort(key=lambda x: x[-1], reverse=True) ## o key é como vc quer fazer a ordenação // lambda -> função anonima

for i, j in items:
    print(i, "->", j)


# %%
