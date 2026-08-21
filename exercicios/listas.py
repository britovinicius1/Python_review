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
lista = []
while True:
    continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == "S":
        numero = int(input("Digite um número..."))
        if numero not in lista:
            lista.append(numero)
            print("Numero adicionado na lista..")
        else:
            print("Numero ja está na lista...Tente outro número")
    elif continuar == "N":
        lista.sort()
        print(f"A lista digitada foi.. {lista}")
        break
    else:
        print("Digite uma opção valida!!")

##
lista = []
while True:
        numero = int(input("Digite um número..."))

        if numero not in lista:
            lista.append(numero)
            print("Numero adicionado na lista..")
        else:
            print("Numero ja está na lista...Tente outro número")

        continuar = input("Deseja continuar? [S/N]").upper()

        if continuar == "N":
            lista.sort()
            print(f"A lista digitada foi.. {lista}")
            break

# %%
#080)##
##Crie um programa onde o usuário possa digitar 
# cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção 
# (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

lista = []

for i in range(0,5):
    n = int(input("Digite um valor:"))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"Adicionado na pposicao {pos} da lista")
                break
            pos += 1
print('-=' * 30)
print(f"os valores digitados foram {lista}")

#%%
#081)
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    numero = int(input("Digite um número..."))
    lista.append(numero)
    
    continuar = input("Deseja continuar? [S/N]").upper()
    while continuar not in ("S", "N"):
        continuar = input("Opção inválida! Deseja continuar? [S/N]").upper()
    
    if continuar == "N":
        break

qtde_numeros = len(lista)
lista.sort(reverse=True)
print(f"Foi digitado {qtde_numeros} números...")
print(f"Segue a lista ->  {lista}")
if 5 in lista:
    print("O valor 5 foi digitado na lista =)")
else:
    print("O valor 5 não foi encontado na lista...")

#81)
#Crie um programa que vai ler vários números e colocar em uma lista.

#Depois disso, 
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
# respectivamente.
#Ao final, mostre o conteúdo das três listas geradas...





# %%
