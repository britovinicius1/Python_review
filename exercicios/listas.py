#%%
#78)Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor 
# valor digitado e as suas respectivas posições na lista.

lista = []
for i in range(5):
    valor = int(input(f"Insira o numero {i}"))
    lista.append(valor)

maior = lista[0]
menor = lista[0]

for pos,numero in enumerate(lista):
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"O maior numero da lista foi {maior} na posicao {lista.index(maior)}")
print(f"O maior numero da lista foi {menor} na posicao {lista.index(menor)}")

#%%
lista = []
maior = 0
menor = 0

for i in range(0,5):
    valor = int(input(f"Digite um valor na posicação {i}"))
    lista.append(valor)
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print("=-"*30)

#%%
#079
#Crie um programa onde o usuário possa digitar 
# vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, s
# erão exibidos todos os valores únicos digitados, em ordem crescente.
#







# %%
