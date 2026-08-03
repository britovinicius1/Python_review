#%%
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input("Qual o valor da casa??"))
salario_pessoa = float(input("Digite seu salário:"))
anos_emprestimo = int(input("Em quantos anos você ira comprar a casa?"))
parcela = valor_casa/(anos_emprestimo * 12)
minimo = salario_pessoa  * 0.30

if (parcela) <= minimo:
    print(f"Seu financiamento foi aprovado, \nno valor de R${valor_casa:.2f} e sera financiado em {anos_emprestimo}. Com parcelas de R${parcela:.2f}")
else:
    print(f"O emprestimo foi negado, as parcelas excederam 30% do seu salario\n, pois a parcela é R${parcela} e o minimo que pode ser pego é R${minimo}")


#%%

# 💡 Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero1 = int(input("Digite um número inteiro:"))
numero2 = int(input("Digite o segundo número inteiro:"))

if numero1 > numero2:
    print("O primeiro número digitado é o maior.")
elif numero1 < numero2:
    print("O segundo número é maior")
else:
    print("Números iguais...")

# %%
# 💡 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo...

ano_nascimento = int(input("Digite o ano em que você nasceu:"))
idade = 2026 - ano_nascimento

if idade < 18:
    print(f"Ele ainda vai se alistar, pois só tem {idade} anos..")
elif idade == 18:
    print(f"Você precisa se analistar pois ja completou {idade} anos")
else:
    print(f"Ja passou da idade do alistamento, você tem {idade} anos")
# %%
