#%%

import requests
from tqdm import tqdm
import pandas as pd

ceps = ['01310100', '20040020', '30130110', '41820021', 
        '80010010', '51020000', '64000100', '69010060', 
        '74810100', '90010150']
url = 'https://viacep.com.br/ws/{cep}/json/'

# %%
dados = []
for cep in tqdm(ceps):
    requisicao = requests.get(url.format(cep=cep))
    if requisicao.status_code == 200:
        dados.append(requisicao.json())
# %%
data_set = pd.DataFrame(dados)

# %%
data_set['unidade'] = 'N/D'
# %%
data_set
# %%
data_set['unidade'] = data_set['unidade'].isnull()
# %%
data_set.query("logradouro == 'Avenida Paulista'")
# %%
cep = data_set["cep"]
dados_splitado = []
for i in cep:
    d = i.split('-')
    dados_splitado.append(d)

dados_splitado
# %%
data_set
# %%
data_set[['cep_parte1', 'cep_parte2']] = data_set['cep'].str.split('-', expand=True)
# %%
data_set
# %%
data_set["uf"].value_counts()
# %%
data_set
data_set['complemento'] = data_set['complemento'].replace('', 'N/D')
# %%
data_set
# %%
