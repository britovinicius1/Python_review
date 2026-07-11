#%%
#padrao é retornar uma tupla:
def operacao_basica(a,b):
    lista = []
    soma = a + b
    dif = a - b
    mult = a * b
    lista.append(soma)
    lista.append(dif)
    return soma,dif,mult,lista

print(operacao_basica(2,3))

#%%
meta = 1000
vendas = {
    'Joao': 15000,
    'Vini': 3000,
    'Rovisaldo': 200,
    'Segiao': 40000

}
def calculo_meta(meta,vendas):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    perc_bateram_meta = len(bateram_meta)/len(vendas)
    return perc_bateram_meta, bateram_meta

percent_bateram_meta, vendedor_bateu = calculo_meta(meta,vendas)
print(f"O percentual de pessoas que bateram a meta: {percent_bateram_meta}\n"
      f"foram eles{vendedor_bateu}")
# %%
