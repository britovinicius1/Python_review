#%%
#percore uma lista só que de forma mais direta.
#for em uma linha de código
# lista = [expressão for item in iterable]
#Normalmente isso é usado quando queremos fazer uma única ação com itens de uma lista
#se a lista for uma muto grande, o list vai travar acaba sendo dificil compilar.


preco_produtos = [100, 150, 300, 5500]
produtos = ["vinho", "cafeteira","microondas","iphone"]

impostos = []
for item in preco_produtos:
    impostos.append(item * 0.3)
print(impostos)
# %%

impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)
# %%
def calcular_imposto(preco,impostos):
    return preco * impostos

#%%
impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]
# %%
print(impostos)
# %%
preco_produtos = [100, 150, 300, 5500]
produtos = ["vinho", "cafeteira","microondas","iphone"]
#%%
#zipa
lista_aux = list(zip(preco_produtos,produtos))
lista_aux.sort(reverse=True)
print(lista_aux)
# %%
produtos_finalizado = [produto for venda,produto in lista_aux]
print(produtos_finalizado)
# %%
#1))) TIrando iformações de listas e dicionarios
#criar uma lista de 2019 
vendas_produtos = [
    ('iphone', 58147, 951642),   # primeiro número pode estar errado, tá cortado
    ('galaxy', 712350, 244295),
    ('ipad', 573823, 26964),
    ('tv', 405252, 787604),
]

lista_venda2019 = []
for produto, venda2019,venda2020 in vendas_produtos:
    lista_venda2019.append(venda2019)
print(lista_venda2019)

# %%
lista_vendas_2019_2 = [vendas2019 for produto, vendas2019,vendas2020 in vendas_produtos]
print(lista_vendas_2019_2)
# %%
print(max(lista_vendas_2019_2))

# %%
lista_vendas_2019_produtos = [(vendas2019,produto) for produto, vendas2019,vendas2020 in vendas_produtos]
# %%
print(max(lista_vendas_2019_produtos))
# %%
