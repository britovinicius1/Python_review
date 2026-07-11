#%%

def f(x):
    resultado = 1 + x
    return resultado

#%%
valor = f(10)
print(valor)

# %%
# Tem que ser na mesma ordem...
#a variavel que é definida dentro do escopo da função voce nao consegue acessar fora do escopo
#apenas dentro da função;
#type hint -> dica, lembrando que não força;


def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """Essa função é pra calcular o retorno financeiro após inserir
    Uma taxa, o aporte e a quantidade de anos que vai render;"""
    resultado = aporte * (1+taxa) ** anos
    return resultado
#se definir os valores pode mexer na ordem
juros_compostos(aporte=1000,taxa=0.13, anos=4)


# %%
#função que nao retorna nada
def ola_mundo():
    print("Ola mundo =))")

ola_mundo()
# %%
def par_impar(numero:int):
    if numero % 2 == 0:
        print("O numero é par!!!")
    else:
        print("O numero é impar")
numero = int(input("Entre com um número!!"))
par_impar(numero)

# %%
#é bom deixar as  funções fazendo funcionalidades mais únicas pra poder reaproveitar
#o certo é um arquivo para contexto de funções;

#argumentos opcionais precisam vim depois dos obrigatórios;

def soma(a:float,b:float)->float:
    return a + b

def media(a:float, b:float)->float:
    return soma(a,b) / 2
#### outra forma:


def soma(valores:list)->float:
    return sum(valores)

def media(valores:list)->float:
    return soma(valores) / len(valores)

a = float(input("Entre com um valor a"))
b = float(input("Entre com um valor b"))

media_valor = media([a,b])

print(f"A média do calculo é {media_valor}")

# %%
#tudo que passar sem ser valor nomeado o args absorve

def soma(a:float,b:float,*args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a,b, *args)->float:

    return soma(a,b,*args) / ( len(args) + 2 )

a = float(input("Entre com um valor a"))
b = float(input("Entre com um valor b"))
b = float(input("Entre com um valor c"))

print(media(a,b,c))


# %%
#keywargs -> dicionarios
def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto =  preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto
imposto_final = calc_imposto(3000,0.03, municipio=0.1, nacional=0.01, federal=0.02)
print(f"O imposto foi {imposto_final}")

#%%

impostos_gerais = {
    "mnunicio": 0.1,
    "estadual":0.03,
    "nacional": 0.5

}
calc_imposto(1000,0.03, **impostos_gerais)
