#%%

#readlines cada linha vira uma posição da lista
#ele joga em lista

arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)


## o strip se vc passar um argumento ele ranca oq vc passar das extremidades

#%%
dados = dict()

chaves = lines[0].strip("\n").split(";")
print(chaves)
for c in chaves:
    dados[c] = []


# %%
for l in lines[1:]:

    valores = l.strip("\n").split(";")
    print(valores)
    for i in range(len(valores)):
        print(i)
        dados[chaves[i]].append(valores[i])

    
# %%
print(dados)
# %%
### forma mais simples
dados = {}

with open(arquivo, encoding="utf-8") as file:
    linhas = file.readlines()

chaves = linhas[0].strip().split(";")

for chave in chaves:
    dados[chave] = []

for linha in linhas[1:]:
    valores = linha.strip().split(";")

    for chave, valor in zip(chaves, valores):
        dados[chave].append(valor)

# %%
idades = []
for i in dados["idade"]:
    idades.append(int(i))

# %%
media = sum(idades) / len(idades)
media
# %%
