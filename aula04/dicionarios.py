#Estruturas de dados bem completas na estrutura chave e valor e são mutaveis.
#podem conter dados de tipos diferentes e até outros dicionarios

#%%
dic = {

}

type(dic)
# %%
##exemplo de dicionario
pessoas = {
    'Vini':30,
    'Rafael': 40,
    'pesos': {'Vini':91,'Rafael':72},
    'Valores': [1,2,3,4,5,6],
    'Strings': ['Minerados', 'Data Science', 'Globo.com']
}
print(pessoas['pesos']['Vini'])
print(pessoas['Valores'][0])
print(pessoas['Vini'])
# %%
#atualizando dicionario
pessoas['Vini'] = 30
#apagando elementos
#%%
del pessoas['vini'] #---> apaga uma chave

#### METODOS DOS DICIONARIOS

#%%
pessoas.keys()
pessoas.values()
# %%
#criando outro dict
pessoas2 = {'Norma': 69, 'Josefina': 33}
# %%
pessoas.update(pessoas2)
print(pessoas)
# %%
#retorna o valor da chave caso ela exista, senao retorna o valor do parametro
pessoas.get("Marcos", "não_existe")
# %%
##ele deleta a anterior e da pra armazenar o valor entao vc cria outra variavel por exemplo.
pessoas['Vinicius'] = pessoas.pop('Vini')
# %%
print(pessoas)
# %%
pessoas.setdefault('Marcos', 30) #->>>> retorna a chave caso nao exista ele cria
# %%
print(pessoas)
# %%
pessoas.clear() ##Apaga o conteuodo do dicionario.

#%%


