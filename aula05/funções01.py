#%%
def cadastrar_produto():
    produto = input("Digite o nome do produto que deseja cadastrar")
    produto = produto.casefold()
    produto = produto.strip()
    return produto
# %%
variavel_produto = cadastrar_produto()
print(variavel_produto)
# %%

def somar (v1:float,v2:float) -> float:
    """
    um função simples de soma
    """
    v3 = v1 + v2
    return v3

s = somar(2,4)
print(s)

#%%
#%%
list = [20,30,40,50,60,10,11]

list.sort()
print(list)





# %%
