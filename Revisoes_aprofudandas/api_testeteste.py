#%%
import requests
import pandas as pd
#%%

poke = input("Digite um nome de um pokemon:")

url = "https://api.football-data.org/v4/matches/{poke}"

resposta = requests.get(url.format(poke=poke))
# %%
resposta
# %%
