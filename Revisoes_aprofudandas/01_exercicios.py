##1) Crie um programa que tenha um tupla totalmente preenchida com uma contagem extenso, de zero até vinte
##seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostralo por extenso
#%%
numeros = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
    "vinte"
)

continuar = "1"

while continuar == "1":
    numero_digitado = int(input("Digite um número de 0 a 20: "))
    if numero_digitado not in range(0, 21):
        print("Erro!!!, digite um número válido.")
        break
    else:
        print(f"O número digitado foi {numeros[numero_digitado]}")
    
    continuar = input("Quer continuar? 1 - Sim | 2 - Não: ")
    
    while continuar not in ("1", "2"):
        continuar = input("Opção inválida! Digite 1 - Sim ou 2 - Não: ")

    if continuar == '2':
        print("Saindo do programa....")

#%%
#2) Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.
times = (
    "Palmeiras",
    "Flamengo",
    "Fluminense",
    "São Paulo",
    "Athletico Paranaense",
    "Bahia",
    "Red Bull Bragantino",
    "Coritiba",
    "Vitória",
    "Botafogo",
    "Atlético-MG",
    "Internacional",
    "Vasco da Gama",
    "Grêmio",
    "Cruzeiro",
    "Santos",
    "Corinthians",
    "Mirassol",
    "Remo",
    "Chapecoense",
)
print("Os tops colocados do brasileirão são:")

for pos, time in enumerate(times[:5]):
    print(f"{pos+1} - {time}")

print("Os times que estão na zona de rebaixamento são")

for pos, time in enumerate(times, start=1):
    if pos > len(times) - 4:
        print(f"{pos} - {time}")

print("Times em ordem alfabética:")
print(sorted(times))

for pos,time in enumerate(times):
    if time == "Chapecoense":
        print(f"O time {time} está na posição {pos} no campeonato Brasileiro")

#%%

#3) Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
#
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão
# na tupla.

from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10),randint(1,10))
print(n)
print(f"\nO Maior valor sorteado foi {max(n)}")
print(f"O Maior valor sorteado foi {min(n)}")
#%%
numeros = (int(input("Digite um numero:")),
          int(input("Digite um numero:")),
          int(input("Digite um numero:")),
          int(input("Digite um numero:")))

print(f"Você digitou os seguintes números {numeros}")

print(f"O numero 9 apareceu {numeros.count(9)}")

if 3 in numeros:
    print(f"O valor 3 apareceu na {numeros.index(3)+1}ª")
else:
    print("O valor 3 não foi digitado...")

print("Valores pares digitados:")
for n in numeros:
    if n % 2 == 0:
        print(n)

#%%
##4)# Crie um programa que tenha uma tupla única com nomes de
# produtos e seus respectivos preços, na sequência.
#
# No final, mostre uma listagem de preços, organizando
# os dados em forma tabular.
