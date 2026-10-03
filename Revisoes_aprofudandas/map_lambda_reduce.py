#%%
## Função lambda (função anonima) -> nao tem nome e pode ser usada naquele momento
# sintaxe: lambda argumentos: expressão

quadrado = lambda x: x**2

for i in range(1,11):
    print(quadrado(i))

#%%
par = lambda x: x%2 == 0

print(par(9))

#%%
f_c = lambda f: (f-32)*5/9
print(f_c(32))

# %%
# Função map()
# função que aplica funções
# Sintaxe: map(funcao,interavel)
## a funcao que vc vai passar vai ser aplicada pra cada item
#retorno um objeto do tipo map
##função de ordem superior

num = [1,2,3,4,5,6,7]
dobro = list(map(lambda x: x*2, num))
print(dobro)

# %%
palavras = ['Python', 'é', 'bom']
maiusculas = list(map(str.upper, palavras))
print(maiusculas)

# %%
