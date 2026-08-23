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

#%%
#82)
#Crie um programa que vai ler vários números e colocar em uma lista.

#Depois disso, 
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
# respectivamente.
#Ao final, mostre o conteúdo das três listas geradas...

lista = []
lista_pares = []
lista_impares = []
while True:
    numero = int(input("Digite um numero"))
    lista.append(numero)
    resposta = str(input("Quer continuar? [S/N]").upper())
    if resposta == "N":
        print("Lista populada")
        print("="*20)
        break

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
        
lista.sort()
lista_pares.sort()
lista_impares.sort()
print(f"A lista populada foi -> {lista}")
print(f"Segue a lista de pares -> {lista_pares}")
print(f"Lista de impares -> {lista_impares}")

# %%
#83)--->>> Fazer esse depois : Crie um programa onde o 
# usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os 
# parênteses abertos e fechados na ordem correta.

#%%
#084)
#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:

#A) Quantas pessoas foram cadastradas.

#B) Uma listagem com as pessoas mais pesadas.

#C) Uma listagem com as pessoas mais leves.
#
lista_pessoas = []
lista = []
maior = menor = 0
while True:
    nome = str(input("Digite o nome da pessoa:"))
    peso = float(input("Digite o peso da pessoa:"))
    lista.append(nome)
    lista.append(peso)
    if len(lista_pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    lista_pessoas.append(lista[:])
    lista.clear()
    resposta = input("Quer continuar?[S/N]").upper()
    if resposta == "N":
        break

qtde_pessoas = len(lista_pessoas)
print("=" * 30)
print("=" * 15, "informações", "="*15)
print(f"A lista de pessoas cadastrada -> {lista_pessoas}")
print(f"A)Ao todo,foram cadastrado {qtde_pessoas}pessoas...")

print(f"O maior peso foi de {maior}Kg")
for nome,peso in lista_pessoas:
    if peso == maior:
        print(f"[{nome}]")

print(f"O menor peso foi de {menor}Kg")
for p in lista_pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]")


#%%
#085)
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
# em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.


lista_completa = []
lista_pares = []
lista_impares = []
for i in range(0,7):
    numero = int(input(f"Digite o {i+1}º numero: "))
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
lista_pares.sort()
lista_impares.sort()
lista_completa = [lista_pares,lista_impares]
print(f"A lista final -> {lista_completa}")

#%%
#Outra forma mais fácil
lista_numeros = [[],[]]
for i in range(1,8):
    valor = int(input(f"Digite o {i}º número:"))
    if valor % 2 == 0:
        lista_numeros[0].append(valor)
    else:
        lista_numeros[1].append(valor)

lista_numeros[0].sort()
lista_numeros[1].sort()
print(f"Os valores pares digitados foram ->> {lista_numeros[0]}")
print(f"Os valores impares digitados foram ->> {lista_numeros[1]}")


#%%
#086)
#
#Crie um programa que crie uma matriz de dimensão 3x3 e 
# preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.
#



#%%

#087)
#Aprimore o desafio anterior, mostrando no final:

#A) A soma de todos os valores pares digitados.

#B) A soma dos valores da terceira coluna.

#C) O maior valor da segunda linha.
#

#%%
#088)
#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 
# 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.





#%%
#089)Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que 
# o usuário possa mostrar as notas de cada aluno individualmente.
#
#
#

