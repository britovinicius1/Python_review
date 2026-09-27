#%%
#Você vai construir um mini sistema que 
# registra vendas de uma loja e gera relatórios, usando *args e **kwargs.

def registrar_venda(vendedor: str, *produtos:str, **detalhes):

    """
    -> Função que registra dados de vendas.
    Args:
        Vendedor: Nome do vendedor
        Produtos: produtos comprados na venda
        detalhes: detalhes de vendas
    Retorno:
        Retorna um dicionario com as informações de vendas
    """

    lista_produtos = []
   
    for i in produtos:
        lista_produtos.append(i)

    venda = {
            "vendedor": vendedor, 
            "produtos": lista_produtos, 
            "detalhes": detalhes}

    return venda

def relatorio(*vendas):
    """
    -> Função que recebe várias vendas cadastradas
    """
    
    total_produtos = 0
    total_vendas = len(vendas)
    

    for venda in vendas:
        qtd_produtos = len(venda["produtos"])
        total_produtos += len(venda["produtos"])
        
        lista_produtos = ""

        for produto in venda["produtos"]:
            lista_produtos = lista_produtos + produto + ", "

        lista_produtos = lista_produtos[:-2] + "!"

        print(f"# {venda['vendedor']} vendeu {qtd_produtos} produto(s): {lista_produtos}")
    
    print("\n")
    print(f" -> Total de vendas registradas: {total_vendas}")
    print(f" -> Total de produtos vendidos: {total_produtos}")


def total_por_vendedor(*vendas):

    total_vendedor = {}

    for venda in vendas:
        nome_vendedor = venda['vendedor']
        qtd_produtos = len(venda['produtos'])

        if nome_vendedor in total_vendedor:
            total_vendedor[nome_vendedor] += qtd_produtos
        else:
            total_vendedor[nome_vendedor] = qtd_produtos 

    return total_vendedor
           
## PROGRAMA PRINCIPAL
print("="*15,"Relatório de vendas", "="*15)
print("="*51)

venda_1 = registrar_venda(
    "Vinicius",
    "Televisão",
    "Iphone",
    "celular",
    forma_pagamento = "Pix",
    desconto = 0.1)

venda_2 = registrar_venda(
    "Luana",
    "Playstation",
    "Fone",
    "teclado",
    forma_pagamento = "Pix",
    desconto = 0.1)

venda_3 = registrar_venda(
    "Rafael",
    "PS5",
    "Forno",
    "MacBook PRO",
    forma_pagamento = "Pix",
    desconto = 0.2)

venda_4 = registrar_venda(
    "Vinicius",
    "Computador",
    "Iphone pro max",
    "Nike",
    "Cabo USB",
    forma_pagamento = "Crédito",
    desconto = 0.15)

lista_vendas = [venda_1,venda_2,venda_3,venda_4]

relatorio(*lista_vendas)
print(total_por_vendedor(*lista_vendas))







### programa principal

# %%

