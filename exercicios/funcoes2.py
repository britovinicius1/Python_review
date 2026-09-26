#%%
#Exercicio pratico

def fatorial(num = 1):
     f = 1
     for c in range(num,0,-1):
           f *= c
     return f

n = int(input("Digite um numero: "))
f1 = fatorial(n)
print(f1)
# %%

def imprimir_itens(lista):
      for item in lista:
            print(item)
l1 = [1,2,3,4]
l2 = ["vini", "joao","rafael"]
l3 = ["12", "vinicius", 14.44]

imprimir_itens(l3)
# %%

def mostrar_inicio_processamento(numero_pedido):
      print(f"Iniciando processamento do pedido #{numero_pedido}")

mostrar_inicio_processamento(25)

# %%
def calcular_desconto(preco: float, 
                      quantidade: int, 
                      desconto: float
                      ) -> float:
      """
      Calcula o valor final de um item após aplicar o desconto

      Args:
        preco: precço unitario do produto
        quantidade: quantidade comprada
        desconto: Percentual de desconto em formato decimal

      Returns:
        Valor final da compra
      """
      
      subtotal: float = preco * quantidade
      valor_desconto: float = subtotal * desconto
      total: float = subtotal - valor_desconto

      return total

valor_pedido = calcular_desconto(90,9,0.5)
print(valor_pedido)
# %%
help(calcular_desconto)

# %%
#### *args -> empacota como tupla, vc pode passar diversos argumentos para função
def cadastrar_produtos(
            nome:str,
            preco: float,
            estoque: int
) -> None:
      print(f"Produto: {nome}")
      print(f"Preço:R${preco}")
      print(f"Estoque:{estoque}")

cadastrar_produtos("Teclado", 150, 20)
# %%
def cacular_total(*valores:float) -> float:
      print(valores)
      return sum(valores)

total2 = cacular_total(20,30,50,40)
print(total2)
# %%

def calcular_total_pedido(*valores: float) -> float:
      total = 0

      for valor in valores:
            total += valor

      return total

total3 = calcular_total_pedido(
      120,
      89.90,
      490.10
)

print(total3)
# %%

def registrar_pedido(
            numero_pedido: int,
            *produtos: str
) -> None: 
      print(f"Pedido #{numero_pedido}")

      for produto in produtos:
            print(f"- {produto}")

registrar_pedido(
      1024,
      "Notebook",
      "Mouse",
      "Fone de ouvido"
)
# %%
## **kwargs -> argumento nomeado, ele traz um dicionario
#junta todos nomeados em um dicionario

def cadastrar_clientes(**dados) -> None:
      for chave, valor in dados.items():
            print(f"{chave} -> {valor}")


cadastrar_clientes(
      nome="Vini",
      email="vini@hotmail.com",
      cidade="Passos"
)

# %%

def cadastrar_clientes_novo(
            nome: str,
            email: str,
            **dados_adicionais
) -> None:
      print(f"Nome: {nome}")
      print(f"Email: {email}")

      for k,v in dados_adicionais.items():
            print(f"{k} ->> {v}")

cadastrar_clientes_novo(
      nome="Vini",
      email="vini@hotmail.com",
      cidade="Passos",
      estado="MG",
      profissao = "Data Analyst"

)
# %%
def registrar_venda_novo(
            cliente: str,
            *produtos: str,
            **dados_adicionais:str
) -> None:
      print(f"#Cliente {cliente}")

      print("\nProdutos")

      for produto in produtos:
            print(f" - {produto}")

      print("\nInformações:")

      for k,v in dados_adicionais.items():
            print(f"{k.capitalize()}: {v}")

registrar_venda_novo(
      "Vinicius",
      "Notebook",
      "Telefone",
      forma_pagamento = "Pix",
      vendedor = "Caio",
      entrega = True
)
# %%
