#%%
import requests
import pandas as pd
#%%

poke = input("Digite um nome de um pokemon:")

url = "https://pokeapi.co/api/v2/pokemon/{poke}"

resposta = requests.get(url.format(poke=poke))

#%%
if resposta.status_code == 200:
    dados = resposta.json()

    stats = {}
    for s in dados['stats']:
        nome_stat = s['stat']['name']
        valor_stat = s['base_stat']
        stats[nome_stat] = valor_stat
#%%
##

print(stats)
#%%
dados_final = pd.DataFrame([stats])

# %%
dados_final
# %%
