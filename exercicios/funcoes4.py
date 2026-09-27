#%%

def cadastrar_produto(
        nome: str,
        preco: float,
        estoque: int = 0
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque}")


produto = ["Teclado", 4500, 120]
produto2 = ("Notebook", 5000, 20)

##desempacota a lista nesse caso
cadastrar_produto(*produto)


#%%
##desempacotar com ** ele desempacota o dicionario (desempacota com argumentos nomeados)

produto = {
    "nome": "Mouse",
    "preco": 4500,
    "estoque": 8
}

cadastrar_produto(**produto)

#%%
def calcular_desconto(
        preco: float,
        desconto: float,
        / ##tudo que aparece antes da / deve ser pasado como um arg posicional (obrigatório posicional)
) -> float:
    return preco - (preco * desconto)

calcular_desconto(500,0.10)

#%%
##atenção isso não é args
def exportar_relatorio(
        nome_arq: str,
        *, ### Depois disso tudo vai necessariamente precisar ser nomeados.
        incluir_cabecalho: str,
        compactar: bool
) -> None:
    print(nome_arq)
    print(incluir_cabecalho)
    print(compactar)

exportar_relatorio("vendas.csv", incluir_cabecalho=True, compactar=True)

#%%
def processar_pagamento(
        numero_pedido: int, #obrigatorio posicional
        valor: float, #obrigatorio posicional
        /, #tudo a esquerda deve ser posicional
        forma_pagamento:str, #nao tem restri 
        *, ## -> separador que indiica que tudo que está a direita deve ser passado como nomeado
        enviar_comprovante: bool = True #obrigatorio nomeado
) -> None:
    print(f"Pedido: {numero_pedido}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Enviar comprovante: {enviar_comprovante}")
# %%
processar_pagamento(
    1050,
    500,
    "Pix",
    enviar_comprovante=True
)
#%%
## RESUMO
def funcao(
        a, #obrigatório posicional
        b, #obrigatório posicional
        /, #diz que tudo que vem antes deve ser posicional
        c,  #tanto faz
        d, #tanto faz
        *args, # Numero variavel de argumentos posicionais -> 
        e, ##obrigatoriamente nomeado pq o args pra traz ja vai pegando os outros posicionais
        f, ##obrigatóriamente noemado
        **kwargs ##argumentos nomeados
):
    print(f"A -> {a}")
    print(f"B -> {b}")
    print(f"C -> {c}")
    print(f"D -> {d}")
    print(f"*args -> {args}")
    print(f"e -> {e}")
    print(f"f -> {f}")
    print(f"**kwargs -> {kwargs}")

funcao(
    1,
    2,
    3,
    4,
    6,
    7,
    8,9,10,11,12,
    e=13,
    f=14,
    nome="Vini",
    estado="MG"
)

# %%
