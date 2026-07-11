#%%
####
#Variavéis compostas
# a = lanche -> variavel simpls
## listas, tuplas e dicionarios
#tuplas os elementos tem indices 0,1,2,3,4
# a = (1,2,3,4)
    ## 0,1,2,3
## as tuplas são imutavel -> não é possivel mudar valores da tupla
##enquanto o programa tiver rodando
##string são variavéis compostas
## fatiamento ->> [0:2] -> o ultimo é ignorado.
## -1 ->> traz o ultimo
## len() ->>> traz o tamanho

#%%
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
lanche2 = 'Hamburger', 'Suco', 'Pudim'
print(lanche[1])
# %%
lanche[0] = 'Pizza'
# %%
print(lanche2)

# %%
print(lanche[:4])

# %%
for comida in lanche: ##### aqui ele nao traz a posição
    print(comida) 
# %%
for cont in range(0,len(lanche)): ##começa do 0 e vai até o tamanho da tupla
    print(lanche[cont])
# %%
for pos,comida in enumerate(lanche): ####aqui ele traz a posição e o valor
    print(f"Eu vou comer {comida} na posicação {pos}")
# %%
print(sorted(lanche)) #### ele traz em ordem alfabetica
# %%
a = (2,3,4,4)
b = (5,8,1,2)

# %%
print(b)
# %%
c = a + b #### a ordem importa por conta da posição
print(c)
# %%
print(c.count(4))

# %%
print(c.index(4,3))
# %%
pessoa = (2,3,4,'Vinicius') ####pode ter dados de diferentes tipos

# %%
print(pessoa)
# %%
del(pessoa)

# %%
print(pessoa)
# %%
