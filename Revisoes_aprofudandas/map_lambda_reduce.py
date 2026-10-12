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
#Função filter -> filtra elemenos de uma sequência
#sintaxe: filter(funcao, sequencia)

def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,10,20,40,23,25,66,40]

num_par = list(filter(numeros_pares, numeros))

num_par

#%%
numeros = [1,2,3,4,5,6,10,20,40,23,25,66,40]

num_impar = list(filter(lambda n: n % 2 != 0, numeros))

num_impar

# %%
##função reduce;
#Sintaxe: reduce(funcao, sequencia, valor_inicial)
#ele faz uma operação cumulativa, fazendo cada uma e dps vai acumulando

from functools import reduce

def mult(x,y):
    return x * y

numeros = [1,2,3,4,5,6] # 1*2*3*5*6 (faz um fatorial !)

total = reduce(mult, numeros)
total

# %%
from functools import reduce

def mult(x,y):
    return x * y

numeros = [1,2,3,4,8,22,44] # 1*2*3*8*22,44 (faz um fatorial !)

total = reduce(mult, numeros)
total

#%%
# ((1² + 2²) + 3²)² + 4²
numeros = [1,2,3,4]

total = reduce(lambda x,y: x**2 + y**2, numeros)
print(total)
# %%
