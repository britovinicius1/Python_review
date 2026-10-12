#%%
# 1. Tirando informações de listas e dicionários

# Digamos que você está analisando as vendas de produtos de uma empresa de varejo.

# Essa lista tem: (produto, vendas de 2019, vendas de 2020) para cada produto.

# Crie uma lista com as vendas de 2019.


vendas_produtos = [
    ('iphone', 558147, 951642),
    ('galaxy', 712350, 244295),
    ('ipad', 573823, 26964),
    ('tv', 405252, 787604),
    ('maquina de café', 718654, 835288),
    ('kindle', 531580, 158883),
    ('geladeira', 973139, 366128),
    ('adega', 892292, 989399),
    ('notebook', 422387, 673234),
    ('fone bluetooth', 385911, 541020),
]

lista_auxiliar = []
for produto, venda_2019,venda_2020 in vendas_produtos:
    lista_auxiliar.append(venda_2019)
# %%
lista_auxiliar
# %%
# com list compreheension

lista_vendas_2019 = [venda_2019 for produto,venda_2019,venda_2020 in vendas_produtos]
lista_vendas_2019
print(f"O maior valor é {max(lista_vendas_2019)}")
# %%
### exercicio 02)
# dica, lista dicionario, tupla e quer criar outra lista...
## Exercícios

### 1. Filtrar lista de clientes inadimplentes

# - O objetivo é identificar quem são os clientes inadimplentes e enviar essa lista de clientes para o setor de cobrança poder fazer a cobrança dos clientes.
# - Queremos então criar uma lista com os clientes inadimplentes (apenas o CPF e o valor que eles estão devendo)
# - A inadimplência nessa empresa é calculada da seguinte forma:
#     1. Se o cliente tiver devendo há mais de 20 dias, ele é considerado inadimplente.
#     2. As informações vêm no formato (cpf, valor_devido, qtde_dias_devendo)

clientes_devedores = [
    ('462.286.561-65', 14405, 24),
    ('251.569.170-81', 16027, 1),
    ('297.681.579-21', 8177, 28),
    ('790.223.154-40', 9583, 15),
    ('318.774.902-06', 2350, 20),
    ('905.142.367-58', 4120, 21),
    ('127.836.495-72', 780, 5),
    ('584.019.326-90', 22310, 45),
    ('639.457.081-13', 1299, 19),
    ('872.360.514-29', 6750, 33),
    ('043.918.275-64', 310, 2),
    ('716.205.849-37', 18940, 60),
    ('359.682.710-85', 5425, 20),
    ('201.947.638-02', 12090, 30),
    ('684.531.092-47', 975, 10),
]

clientes_inadip = [ (cpf,valor_devido,qtd_dias_devendo,"Inadimplente") for cpf, valor_devido, qtd_dias_devendo in clientes_devedores if qtd_dias_devendo > 20]
clientes_cpfs = [cpf for cpf, valor_devido, qtd_dias_devendo in clientes_devedores if qtd_dias_devendo > 20]
print(clientes_inadip)

# %%
### exercicio 03)
#### Exercícios

### 1. Tamanho do Pedido de Compras
## Exercícios

### 1. Tamanho do Pedido de Compras
#Nesse exercício vamos avaliar o estoque de uma empresa. Vamos considerar que todos os 
#produtos dessa empresa são comprados em lotes de 500 unidades.
# - Caso o estoque esteja abaixo de 1000 unidades, devemos fazer um pedido de 500 unidades.
# - Caso o estoque esteja abaixo de 200 unidades, devemos fazer um pedido de 1000 unidades.

# Defina o valor a ser pedido de cada produto para enviar ao time de compras.

estoque = [
    ('BSA2199', 396), ('PPF5239', 251), ('BSA1212', 989), ('PPF2154', 449),
    ('BEB3410', 241), ('PPF8999', 527), ('EMB9591', 601), ('BEB1020', 150),
    ('PPF7731', 1000), ('BSA4408', 1250), ('EMB3302', 199), ('BEB5567', 200),
    ('PPF0912', 35), ('BSA8820', 999), ('EMB7745', 2300),
]
#%%
lista_pedido = []
for produto,qtd in estoque:
    if qtd < 200:
        lista_pedido.append(1000)
    else:
        lista_pedido.append(500)
lista_pedido
#%%
lista_pedido_v2 = [1000 if qtd < 200 else 500 for produto,qtd in estoque]
lista_pedido_v2
# %%
