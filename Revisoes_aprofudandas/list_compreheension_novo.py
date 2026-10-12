#%%
#####################  Descrição ##################
#List Comprehension é uma forma de iterar pelos elementos das listas de maneira “mais direta”, 
# #com mais “cara de Python”
#em resumo: é como se você fizesse um “for” em 1 linha de código
# usar list comprehension caso seja mais simples, se for algo mais complexo, faça tradicional.

#iteravel em lista de forma simplificada
## sintaxe [expressão for item in lista]

numeros = [2,4,6,7,9,22,21]

quadrados = list(map(lambda n: n**2, numeros))
quadrados
# %%
## com list compreheension

quadrados = [num**2 for num in numeros]
quadrados

# %%
# criar uma lista de números de pares de 0 a 10

pares = [num for num in range(11) if num % 2 == 0]
pares
# %%
frase = "A logica é apenas o principio da sabedoria, e nao o seu fim"

vogais = ["a", "e","i", "o", "u", "é", "á", "í", "ú"]

lista_vogais = [v for v in frase if v in vogais]
len(lista_vogais)
# %%
## Distributiva entre valores de duas listas

distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)
# %%
preco_produtos = [100,150,300,5500]
produtos = ["vinho", "cafeteira", "microondas", "iphone"]

impostos = [preco * 0.3 for preco in preco_produtos] ##pra cada item dentro da lita, faz preco * impostos
impostos
# %%
preco_produtos = [100,150,300,5500]
produtos = ["vinho", "cafeteira", "microondas", "iphone"]

def calcular_impostos(preco, imposto):
    return preco * imposto

impostos = [calcular_impostos(item, 0.3) for item in preco_produtos]
impostos

# %%
preco_produtos = [100,150,300,5500]
produtos = ["vinho", "cafeteira", "microondas", "iphone"]
impostos = [(lambda preco: preco * 0.3)(item) for item in preco_produtos] ##esse item chama a função
impostos


# %%
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ["vinho", "cafeteira", "microondas", "iphone"]

lista_auxiliar = list(zip(vendas_produtos, produtos)) ##zipa, ele junta as duas listas
lista_auxiliar
# %%
lista_auxiliar.sort(reverse=True)
lista_auxiliar
produtos = [produto for vendas,produto in lista_auxiliar]
# %%
produtos
# %%
## com if pra filtrar -> coloca a condição depois lista = [expressao for item in iterable if condicao]

meta = 1000
vendas_produtos = [1500,150,2100,1950]
produtos = ["vinho", "cafeteira", "microondas", "iphone"]

produtos_acima_meta = []
for i,produto in enumerate(vendas_produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)
print(produtos_acima_meta)

#%%
## Mesma coisa só que com list comprehension
produtos_acima_meta_v2 = [produto for i,produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta_v2)
# %%
# list comprehension com if pra escolher o resultado final
## estrutura lista = [item if condicao else outro_resultado for item in iterable]
# o bonus é 10% do valor de endas dele, caso ele tenha batido a meta

vendedores_dic = {
    'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500,
    'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 1000,
    'Carlos': 950, 'Mariana': 2100, 'Pedro': 1001, 'Fernanda': 650,
}
meta = 1000
#%%
bonus = []

for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] * 0.1)
    else:
        bonus.append(0)
print(bonus)

#%%
## com list compreheension
bonus_vendedores = [vendedores_dic[item] * 0.1 if vendedores_dic[item] > meta else 0 for item in vendedores_dic]
bonus_vendedores

# %%
## List comprehensio não serve só pra criar uma lista, serve pra qualquer ação em iterable
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'suco de uva', 'fanta', 'sprite', 'heineken', 'budweiser', 'corona', 'gatorade', 'leite de castanha', 'energético', 'kuat', 'schweppes', 'itaipava']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']

#%%

#Quantos % das venads o meu top 5 produtos representa das vendas totais

total_top_5 = 0
for i,produto in enumerate(produtos):
    if produto in top5:
        total_top_5 += vendas[i]

representatividade_top_5 = total_top_5/sum(vendas)
print(total_top_5)

print(f"Top 5 representou {representatividade_top_5:.1%} das vendas")
# %%
total_top_5_v2 = sum([vendas[i] for i, produto in enumerate(produtos) if produto in top5])
total_top_5_v2
# %%
