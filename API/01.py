#%%

##quando vc acessa um site -> get, clica no link get (obtem alguma info, navegando, solicitando infos)
## API devolve um json


import requests

url = "https://viacep.com.br/ws/01001000/json/"

resposta = requests.get(url)

# %%
#responsa 200: status ok -> fez a requisão e foi aceita
print(resposta)
# %%
resposta.text
# %%
dados = resposta.json()
type(dados)

# %%
dados
# %%
