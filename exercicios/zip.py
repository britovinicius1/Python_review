#%%
#01)

notas = [
    [8, 7, 9],
    [6, 5, 8],
    [10, 9, 10]
]

medias = []

for index,notas in enumerate(notas):
    print(f"Nota do aluno {index+1}:")
    media = round(sum(notas)/len(notas),2)
    medias.append(media)
    for i,nota in enumerate(n):
        print(f"Nota inidividual P{i+1}:{nota}")
        
print(f"A média dos alunos -> {medias}")
    

# %%
produtos = ["Shampoo", "Sabonete", "Creme"]
precos = [25.90, 4.50, 32.00]

for produto, preco in zip(produtos,precos):
    print(f"{produto}: {preco}")
    valor_total = sum(precos)
print(f"o valor total dos produtos {valor_total}")    

# %%
#03)
colunas = ["Nome", "Idade", "Cidade"]

valores = [
    ["João", "25", "São Paulo"],
    ["Maria", "30", "Rio de Janeiro"],
    ["Pedro", "28", "Curitiba"]
]

pessoas = {}

for i in colunas:
    pessoas[i] = []

for linha in valores:
    for coluna, valor in zip(colunas,linha):
        pessoas[coluna].append(valor)

print(pessoas)

# %%
lista = [1,2,3]
nome = ["vini", "rafa", "Joao"]
print(list(zip(lista,nome)))

# %%
