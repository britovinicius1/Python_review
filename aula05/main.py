#%%
from etl import ler_csv_transformar, filtra_produtos_entregues, somar_valores

path_arquivo = "vendas.csv"

lista_deprodutos = ler_csv_transformar(path_arquivo)
produtos_entregues = filtra_produtos_entregues(lista_deprodutos)
print(produtos_entregues)
# %%
