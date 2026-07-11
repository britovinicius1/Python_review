#%%

arquivo = "vendas.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines() #-> lista de linhas

for l in lines:
    print(l)

chaves = lines[0].strip("\n").split(",")

dados_dict = dict()
for c in chaves:
    dados_dict[c] = []

dados_dict


# %%  
for l in lines[1:]:

    valores = l.strip("\n").split(',')

    for i in range(len(valores)):

        dados_dict[chaves[i]].append(valores[i])
# %%
idades = [

]
for i in dados_dict["price"]:
    idades.append(int(i))

media = sum(idades) / len(idades) 
media
# %%
