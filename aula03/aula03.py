## Controle de fluxo#%%
#%%
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
# %%
#Exercicio 1:
#Você está analisando um conjunto de dados de vendas e precisa
# garantir que todos os registros tenham valores positivos para quantidade
#e preço. Escreva um programa que verifique esses campos e imprima dados validos se for positivo e dados invalidos caso negativo

a = int(input("Insira um numero:"))
q = int(input("Digite a quantidade "))

if a > 0 and q > 0:
    print("Dados validos para uso..")
else:
    print("Dados invalidos...")
# %%
#ele nao chega no ultimo valor, caracteristica de range

for i in range(5):
    print(i)

#%%
lista_words = ['Cat', 'Dog', 'Penis']

for word in lista_words:
    print(word)
# %%
texto = 'Hoje é nossa segunda aula de botcamp segunda t t t'

palavras = texto.split(" ")
contagem_palavras = {}

for p in palavras:
    if p in contagem_palavras:
        contagem_palavras[p] +=1
    else:
        contagem_palavras[p] = 1

print(contagem_palavras)

# %%
