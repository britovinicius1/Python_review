## Alguns exercicios de loops
#1)Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
#%%
texto = 'O passaro na floresta cantou a noite toda, a noite toda'
palavras = texto.split(" ")
contagem_palavras = {}

for p in palavras:
    if p in contagem_palavras:
        contagem_palavras[p] += 1
    else:
        contagem_palavras[p] = 1

print(contagem_palavras)

# %%
#2)Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = []
for x in numeros:
    normalizados.append((x - minimo) / (maximo - minimo))

print(normalizados)
# %%
#Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = range(1,10)

for i in numeros:
    if i % 2 == 0:
        print(f"O nunero {i} é par..")
    else:
        print(f"O numero {i} é impar..")

# %%
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "eletrônicos", "valor": 1900}
]
total_por_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria["categoria"] = total_por_categoria["categoria"] + valor
    else:
        total_por_categoria["categoria"] = valor

# %%
