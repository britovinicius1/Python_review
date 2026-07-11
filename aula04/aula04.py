##type hint

idade:int = 30
altura:float = 1.75
nome: str = 'Alice'

#%%
##tipos complexos
produto1:str = "sapato"
produto2:str = "camiseta"
produto3:str = "viodegame"

produtos:list = []

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)
produtos.pop()
print(produtos)
# %%
#dicionarios
import json
produto01 = {
    "nome":"Sapato",
    "tamanho": 31,
    "preco": 6000,
    "reciclavel": True
}

produto02 = {
    "nome":"Televisao",
    "pol": 29,
    "preco": 3200,
    "SmartTV": True
}

# %%
carrionho = []
carrionho.append(produto01)
carrionho.append(produto02)
# %%
print(carrionho)
# %%
##json é o dict do python no javascript
#falar python com javascript -> json com o dict
carriho_json = json.dumps(carrionho)
print(carriho_json)
#_-------------------------------------------------------------
