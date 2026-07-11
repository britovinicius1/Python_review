##tuplas -> Estruturas de dados similares a listas porém são imutavesi
#elas nao podem ser mudadas apos sua criação
#%%
tupla = ('Ferrari', 'Onça', 17, 1299)
print(tupla)
tupla[0] = 1 #->>>> vai da erro, nao da pra atualizar
# %%
tupla_aninhada = (1,2,3, (23,34,43))
print(tupla_aninhada)
# %%
2 in tupla_aninhada
# %%
#conversão de lista em tupla
lista = [1,2,3,4,2.99, 'vini']
tupla3 = tuple(lista)
type(tupla3)
# %%
print(tupla3)
# %%
