#%%
import csv

path_arquivo = "vendas.csv"

def ler_csv_transformar(path_arquivo: str) -> list[dict]:
    dados = []
    with open(path_arquivo, mode="r", encoding="utf-8") as file:
        leitor_csv = csv.DictReader(file)
        for linha in leitor_csv:
            # Adiciona cada linha (um dicionário) à lista de dados
            dados.append(linha)
    return dados

def filtra_produtos_entregues(lista:list[dict]) -> list[dict]:
    lista_de_produtos_entregues = []
    for produto in lista:
        if produto.get("entregue") == "False":
            lista_de_produtos_entregues.append(produto)
    return lista_de_produtos_entregues

def somar_valores(lista = list[dict]) -> int:
    valor_total = 0
    for produto in lista:
        valor_total += int(produto.get("price"))
    return valor_total
# %%
