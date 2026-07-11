#%%

def ehalcolico(bebida):
    bebida = bebida.upper()
    if 'BEB'in bebida:
        return True
    else:
        return False

produtos = [
    'beb46275',
    'TFA23962',
    'TFA69555',
    'BSA45510',
    'CAR75448',
    'CAR23596',
    'bebo2312319'
]

for produto in produtos:
    if ehalcolico(produto):
        print(f"Enviar o produto {produto} para o setor de bebida alcoolicas!")


#%%

def categoria_bebida(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        False

produtos = [
    'beb46275',
    'TFA23962',
    'TFA69555',
    'BSA45510',
    'BSAT1312',
    'CAR75448',
    'CAR23596',
    'bebo2312319',
    'XBI102312023'
]

for produto in produtos:
    if categoria_bebida(produto, 'BEBO'):
        print(f"{produto} é da categoria alcoolica")
    elif categoria_bebida(produto, "BSA"):
        print(f"Produto {produto} não alcoolico")

#%%
#1)calculo de carga tributaria
def carga_tributaria(preco:int, custo:int, lucro:int):
    """Essa é uma função que calcula a carga tributária"""
    imposto = preco - custo - lucro
    carga = imposto / preco
    return carga

preco = 1500
custo = 400
lucro = 800

carga_tributaria_1 = carga_tributaria(preco,custo,lucro)
print(f"O preço do produto foi {preco} com uma carga tributaria de {carga_tributaria_1}")

#%%
#2)
def padronizar_codigos(lista_codigos, padrao='m'):
    for i,item in enumerate(lista_codigos):
        item = item.replace('  ', '')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos

cod_produtos = [' AC12', 'abc34', 'AbC37']
print(padronizar_codigos(cod_produtos, 'M'))


#3)
## lista de emails

def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada

lista_emails = ['vini@hotmail.com', 'zezin@gmail.com', 'jusefino@gmail.com', 'penisvaldo@gmail.com']

lista = filtrar_lista_texto(lista_emails, 'gmail')
print(lista)

# %%
def bateu_meta(vendas,meta):
    if vendas >= meta:
        return True
    else:
        return False

if bateu_meta(150,500):
    print("O funcionario bateu a meta!!")
else:
    print("O funcionario nao batue a meta")
# %%

