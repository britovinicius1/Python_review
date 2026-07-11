#%%

import requests

cep = input("Entre com um cep válido:")

url = 'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url.format(cep=cep))

if resposta.status_code == 200:
    print(resposta.json())
# %%
