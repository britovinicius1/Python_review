#%%

lista_de_numeros = [39,40,22,10,11,25,66,150]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_numeros = numeros.copy()
    for i in range(len(lista_de_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]
    return nova_lista_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
print(nova_lista)

# %%
