#%%
#enumerate pega o index da lista
meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

#%%
produtos_acima_meta = []
for i,produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)
print(produtos_acima_meta)
# %%
produtos_acima_meta2 = [produto for i,produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta2)
# %%
##Filtrar lita de clientes inadimplentes..]
#cliente, venda, dia
#passou de 20 dias inadimplentes
clientes_devedores = [
    ('462.286.561-65', 14405, 24),
    ('251.569.170-81', 16027, 1),
    ('297.681.579-21', 8177, 28),
    ('790.223.154-40', 9582, 35),
    ('183.442.298-77', 12300, 22),
    ('534.871.902-11', 7650, 5),
    ('621.094.337-58', 19800, 41),
]
#%%
clientes_inadip = []
for cpf, valor, dias in clientes_devedores:
    if dias > 20:
        clientes_inadip.append(cpf)
# %%
print(clientes_inadip)
# %%
clientes_inadip_2_list_compr = [cpf for cpf,valor,dias in clientes_devedores if dias > 20]
# %%

print(clientes_inadip_2_list_compr)
# %%
print(len(clientes_devedores))
# %%
## O bonus é dado por 10% do valor de vendas dele, caso ele tenha batido a meta

vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paula': 650, 'Carlos': 1100, 'Beatriz': 3200}
meta = 1000

#%%
bonus = []
for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] * 0.1)
    else:
        bonus.append(0)
print(bonus)
# %%
bonus = [vendedores_dic[item] * 0.1 if vendedores_dic[item]> meta else 0 for item in vendedores_dic]
print(bonus)
# %%
# 1- Tamanho do pedido de compras
# Caso o estoque esteja abaixo de 1000 unidades, devemos fazser um pedido de 500 unidades
# Caso o estoque esteja abaixo de 200 unidades, devemos fazer um pedido de 1000 unidades
#defina o valor a ser pedido de cada produto para enviar ao time de compras
estoque = [
    ('BSA2199', 396),
    ('PPF5239', 251),
    ('BSA1212', 989),
    ('PPF2154', 449),
    ('BEB3410', 241),
    ('PPF8999', 527),
    ('EMB9591', 601),
    ('TRX4421', 312),
    ('KLM7734', 178),
    ('ZYP1023', 830),
    ('DFG6612', 95),
    ('QWE8821', 460),
    ('MNB3341', 720),
    ('RTY9982', 55),
    ('HJK2278', 403),
    ('VBN5510', 667),
    ('PLM4423', 134),
    ('OKI8871', 298),
    ('WSX6634', 512),
    ('EDC1129', 877),
    ('RFV7743', 190),
    ('TGB0092', 345),
    ('YHN3312', 623),
    ('UJM5541', 487),
    ('IKO9923', 71),
    ('AZE4456', 934),
    ('QSX7781', 256),
    ('WDC2234', 185),
    ('EFR5567', 803),
    ('TGY8890', 142),
]
# %%

lista_pedido = []
for produto, qtd in estoque:
    if qtd < 200:
        lista_pedido.append(1000)
    else:
        lista_pedido.append(500)

print(lista_pedido)
# %%
lista_pedido2 = [1000 if qtd < 200 else 500 for produto,qtd in estoque]
print(lista_pedido2)
# %%
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaca', 'vinho tinto']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']

total_top5 = 0
for i,produto in enumerate(produtos):
    if produto in top5:
        total_top5 += vendas[i]
print(total_top5)
representatividade = total_top5/sum(vendas)
print(f"Top 5 representou {representatividade:.0%} das vendas")
# %%
#com list comprehension
total_top_5_lcmp = sum(vendas[i] for i,produto in enumerate(produtos) if produto in top5)
repres = total_top_5_lcmp/sum(vendas)
print(f"Top 5 representou {repres:.2%} das vendas")
# %%

# %%
