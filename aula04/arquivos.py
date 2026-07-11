#%%
#with gerador de contexto, abre e fecha o arquivo;
#r-> read

import csv

path: str = "exemplo.csv"

dados = []

with open(file=path, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        dados.append(linha)
        
print(dados)






# %%
