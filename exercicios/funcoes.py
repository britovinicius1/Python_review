#%%
def resumo(titulo, *itens, **detalhes):
    print(f"Título: {titulo}")
    print(f"Itens (tupla): {itens}")
    print(f"Detalhes (dict): {detalhes}")

resumo(
    "Relatório de vendas",
    "Listerine", "Neutrogena", "Tylenol",
    mes="Setembro",
    ano=2026,
    regiao="SP"
)

# %%
marcas = ["Sanpro", "Baby Toiletries"]
info = {"mes": "Outubro", "regiao": "RJ"}

resumo("Outro relatório", *marcas, **info)
# %%
def soma(a, b, c):
    return a + b + c

nums = [1, 2, 3]
soma(*nums)
# %%
#96)"Faça um programa que tenha uma função chamada área(),
#  que receba as dimensões de um terreno retangular 
# (largura e comprimento) 
# e mostre a área do terreno."

def area(h,l):
    area = h * l
    print(f"A area do retangulo é: {area}m²")


h = int(input("Digite a altura do terreno:"))
l = int(input("Digite a largura do terreno:"))

area(h,l)



#%%
#98)"Faça um programa que tenha uma função chamada contador(), ]
# que receba três parâmetros: início, fim e passo e realize a contagem.

#Seu programa tem que realizar três contagens através da função criada:

#a) De 1 até 10, de 1 em 1
#b) De 10 até 0, de 2 em 2
#c) Uma contagem personalizada."
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f"Contagem de {i} até o {f} de {p} em {p}")
    sleep(1.0)
    
    if i < f:
        contador = i
        while contador <= f:
            print(f"{contador}", end=' ')
            sleep(0.5)
            contador += p
    else:
        contador = i
        while contador >= f:
            print(f"{contador}", end=' ')
            sleep(0.5)
            contador -= p

###programa principal

contador(1,10,1)
contador(10,0,2)
print("Agora é sua vez!!!")
ini = int(input("Início"))
fim = int(input("Fim:"))
passo = int(input("Passo:"))
contador(ini,fim,passo)

    
#%%
#99)"Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

#Seu programa tem que analisar todos os valores e dizer qual deles é o maior."
from time import sleep

(2,3,4,5)

def maior(*arg):
    maior = 0
    for pos,numero in enumerate(arg):
        print(f"{numero}", end=" ")
        sleep(0.5)
        if pos == 0:
            maior = numero
        else:
            if maior < numero:
                maior = numero
    print("")
    sleep(0.5)
    print(f"O maior número digitado foi o {maior}!!!")

##inicio

print("="*15, "BEM VINDO AO PROGRAMA!", "="*15)
print("-"*50)

numeros_digitados = []

while True:
    qtd = int(input("Quantos numeros você quer digitar? [Inteiros]"))
    for i in range(0,qtd):
        numero = int(input(f"Digite o numero na {i+1} pos :"))
        numeros_digitados.append(numero)
    break

maior(*numeros_digitados)

#%%
#Dobrando o valor de uma lista

def dobra(list):
    pos = 0 
    while pos < len(list):
        list[pos] *= 2
        pos +=1
valores = [8,4,2,10]
dobra(valores)
print(valores)

























# %%

# %%
