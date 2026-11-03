#%%
import requests #### realiza requisições na web
import json #### para tratar json de listas/dicionarios para json
from tqdm import tqdm

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
]

#%%


url = "https://viacep.com.br/ws/{cep}/json/"
dados = []

for cep in ceps:
    resposta = requests.get(url.format(cep=cep))
    if resposta.status_code == 200:
        dados.append(resposta.json())
    
dados



#%%
dados_novo = []

for cep in tqdm(ceps):
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if resposta.status_code == 200:
        dados_novo.append(resposta.json())


#%%
dados_novo


# %%
print(dados_novo)
# %%
with open("ceps.json", "w", encoding="utf-8") as open_file:
    json.dump(dados_novo, open_file, ensure_ascii=False, indent=4)

# %%
