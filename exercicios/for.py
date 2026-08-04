#%%
import time
for i in range(10,0,-1):
    print(f"{i}..")
    time.sleep(1)
print("BUMMMM!!")
# %%
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for i in range(1,51):
    if i % 2 == 0:
        print(f"O número {i} é par =) ")

#%%
#Faça um programa que calcule a soma entre todos os números ímpares 
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

for i in range(0,500):
    if i % 2 != 0 and i % 3 == 0:
        print(f"O número {i} é impar e divisivel por 3")    

#%%
#Faça uma tabuada de um número que o usuário escolher só que agora utilizando laço for
print("=-"*20)
numero = int(input("Digite um número:"))
print(f"===== Tabuada do {numero} =======")
for i in range(0,10):
    resultado = i * numero
    print(f"{i} x {numero} = {resultado}")
print("=-"*20)
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
#%%
soma = 0
for i in range(0,5):
    numero = int(input(f"Digite o {i+1}º número"))
    if numero % 2 == 0:
        soma = soma + numero
print(f"A soma dos números é {soma}")

##Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#%%
tot = 0
numero = int(input("Digite um numero"))
for i in range(1,numero+1):
    if numero % i == 0:
        print("\033[33m", end='')
        tot+=1
    else:
        print('\033[31m', end='')
    print(i, end='')
if tot <= 2:
    print("O número é primo!!")
else:
    print("O número não é primo!!")





##
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

#Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#%%
contador = 0
for i in range(0,7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i+1}º pessoa"))
    idade = 2026 - ano_nascimento
    if idade > 18:
        contador = contador + 1
print(f"{contador} pessoas são maiores de idade =)")
#Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
#%%
maior = 0
menor = 0
for p in range(0,5):
    peso = int(input(f"Digite o peso da {p+1}º pessoa.."))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"o maior peso digitado foi {maior} e o menor peso digitado foi {menor}")

## %%

# %%
