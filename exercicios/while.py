
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



#064)Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.



# %%
