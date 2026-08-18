#%%
#057)Faça um programa que leia o sexo de uma pessoa, 
# mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = input("Digite o seu sexo: M - Masculo \n F - Feminino")
    if sexo != 'F' and sexo != 'M':
        print("Você digitou a letra errada.. digite novamente")
    else:
        sexo_completo = 'Feminino' if sexo == 'F' else 'Masculino'
        print(f"O sexo selecionado foi {sexo_completo}")

#058)Melhore o jogo do DESAFIO 028 onde o c
# computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


#%%
#059)Crie um programa que leia dois valores e mostre um menu na tela:

# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Crie um programa que leia dois valores e mostre um menu na tela:

numero_1 = int(input("Digite o 1º número: "))
numero_2 = int(input("Digite o 2º número: "))
opcao = 0
while opcao != 5:
    print("O que você deseja fazer?")
    opcao = int(input("[1]-Somar\n[2]-Multiplicar\n[3]-Maior\n[4]-Novos Números\n[5]-Sair do Programa\n"))
    if opcao == 1:
        resultado = numero_1 + numero_2
        print(f"A soma é {resultado}")
    elif opcao == 2:
        resultado = numero_1 * numero_2
        print(f"A multiplicação é {resultado}")
    elif opcao == 3:
        if numero_1 > numero_2:
            maior = numero_1
            menor = numero_2
        else:
            maior = numero_2
            menor = numero_1
        print(f"O maior é {maior} e o menor é {menor}")
    elif opcao == 4:
        numero_1 = int(input("Digite o novo 1º número: "))
        numero_2 = int(input("Digite o novo 2º número: "))
    elif opcao == 5:
        print("Até logo!!.. Saindo do programa")
    else:
        print("Digite um número da lista.")

#%%
#060)Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex:
# 5! = 5x4x3x2x1 = 120

numero = int(input("Digite um numero:"))
fatorial = 1
contador = 1
while contador <= numero:
    fatorial = fatorial * contador
    contador = contador + 1
print(fatorial)

numero = int(input("Digite um número: "))

fatorial = 1
contador = numero
while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

print(f"{numero}! = {fatorial}")


#061)Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#062)Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

#063)Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados 
# e qual foi a soma entre eles (desconsiderando o flag).
#%%
contador = 0
soma = 0
numero = 0
while numero !=999:
    numero = int(input("Digite um número!"))
    if numero != 999:
        soma = soma + numero
        contador = contador + 1
print(f"Foram digitados {contador} e a soma entre os numeros digitados foi {soma}")



#%%
#064)Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


# %%
#)##66
###Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles 
# (desconsiderando o flag).


numero = 0
soma = 0
contador = 0

while True:
    numero = int(input("Insira um número inteiro"))
    if numero == 999:
        break
    soma = soma + numero
    contador = contador + 1
print(f"A soma dos números digitados é {soma} e foram digitados {contador} números")

#%%
#67)
##Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.
while True:
    valor = int(input("Qual tabuada você quer ver?"))
    if valor < 0:
        print("Saindo do programa...")
        break
    print(f"===========Tabuada do {valor} ============")
    for i in range(0,10):
        resultado = i * valor
        print(f"{i} x {valor} = {resultado}")
    print("="*20)

#%%
#68)
#Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador PERDER,
#  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

contador = 0
while True:
    escolha = input("O que você quer, par ou impar? [P/I]").upper()
    if escolha == "P" or escolha == "I":
        numero_jogador = int(input("Digite um número de 0 a 5"))
        numero_computador = random.randint(0, 5)
        soma = numero_jogador + numero_computador

        if soma % 2 == 0:
            resultado = "P"
        else:
            resultado = "I"
        
        if escolha == resultado:
            print("Você ganhou!!")
            contador = contador + 1
        else:
            print("Você perdeu =(...")
            print(f"Porem, no total, você ganhou {contador}x")
            break
    else:
        print("Digite uma informação valida...")
    

#%%
##69)
#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

maior_18 = 0
masculino = 0
mulher_menor = 0

while True:
    continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == "S":
        idade = int(input("Digite a idade da pessoa"))
        sexo = input("Qual o sexo da pessoa? [M/F]").upper()

        if idade > 18:
            maior_18 += 1
        if sexo == "M":
            masculino += 1
        if sexo == "F" and idade < 20:
            mulher_menor += 1

    elif continuar == "N":
        print("Finalizando programa... Tchau =)")
        print(f"no total temos, \nA){maior_18} \nB){masculino} \nC){mulher_menor}")
        break

    else:
        print("Dite uma opção valida... [S/N]")


#%%
#70)
#Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. 
# No final, mostre:

#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.

total = 0 
preco_maior_que_1k = 0
mais_barato = ""
valor_mais_barato = None
while True:
    continuar = input("Quer continuar? [S/N]").upper()

    if continuar == "S":
        nome_produto = input("Qual produto deseja comprar?")
        preco = float(input("Quanto custou o produto?"))
        total = preco + total

        if preco > 1000:
            preco_maior_que_1k += 1

        if valor_mais_barato is None or preco < valor_mais_barato:
            mais_barato = nome_produto
            valor_mais_barato = preco

    elif continuar == "N":
        print(f"A) O total pago foi {total}\n B){preco_maior_que_1k} custam mais que mil \n C){mais_barato} é o produto mais barato")
        break
    else:
        print("Digite uma opcao correta... [S/N]")     


#%%
#71)
#Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.

#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" *30)
print("BANCO VINI".center(30))
print("=" *30)
valor = int(input("Qual valor você gostaria de sacar? R$"))
total = valor
ced = 50
total_cedulas = 0

while True:
    if total >= ced:
        total -= ced
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_cedulas = 0 
        if total == 0:
            break

print("=" *30)
print("Volte sempre...")







# %%
