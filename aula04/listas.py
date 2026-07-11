##LISTAS e METODOS DE LISTAS
#%%
#estruturas de dados versateis.
bixos = ['dog', 'cat', 12312312, 13.9, [0,0,1]]

#slicing passando por todos
bixos[1:]
bixos.remove("dog")
# %%
len(bixos)
# %%
#concatenando listas
lista1 = [1,2,3]
lista2 = [3,4,5]
listac = lista1 + lista2
# %%
"cat" in bixos
max(listac)
# %%
['OLÁ'] * 3
# %%
bixos.append("dragao")
bixos.extend(["chacau","cobra"])
print(bixos)
# %%
bixos.remove("chacau,cobra")
# %%
bixos.count("dog")
#%%
lista = [1,2,44,55,90,23,44]
lista.sort()
print(lista)
