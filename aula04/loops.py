##
#%%
lista = [1,2,3,4]
for i in lista:
    print(i+2)

# %%
texto = 'eae seu safado'
for caracter in texto:
    print(caracter)
# %%
#função zip
indice = [1,2]
linhas = ['Olá mundo, Python é uma linguagem sensacional', 'mineirando dados da cia']
for i,l in zip(indice,linhas):
    print(i,l)
# %%
#loops aninhados
for i in ['1a fase', '2a Fase', '3a Fase']:
    print(i)
    for y in ['Maça', 'Banana', 'uvas']:
        print(y)
        for z in [1,2,3]:
            print(z)

# %%
#instrução break
for letra in "Python":
    if letra == 'o':
        break
    print(f"letra: {letra}")
# %%
for letra in "Python":
    if letra == 'o':
        continue
    print(f"letra: {letra}")
# %%
