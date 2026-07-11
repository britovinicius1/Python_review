#%%
# ) ##1. Classificador de notas
# TITULO #
#Peça ao usuário 5 notas, 
# guarde numa lista e no final mostre a média, 
# a maior nota, a menor nota e se o aluno passou (média >= 6).
i = 0
lista = []
while i < 3:
    nota = int(input("Insira uma nota: "))
    lista.append(nota)
    i += 1

maior_valor = max(lista)
menor_valor = min(lista)
media = sum(lista) / len(lista)

print(f"Maior nota: {maior_valor}")
print(f"Menor nota: {menor_valor}")
print(f"Média: {media}")

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
# %%
# ) 2. Estoque de loja
#Crie um dicionário com 4 produtos e suas quantidades.
# Peça ao usuário um produto e uma quantidade pra comprar. 
# Mostre se tem estoque suficiente, atualize o estoque se tiver, ou avise se não tiver.

produtos = {
    "Televisão": 6,
    "Abajur": 2,
    "Iphone 16": 4,
    "PS5": 2
}

while True:
    print("\n--- ESTOQUE ---")
    for i, j in produtos.items():
        print(f"{i}: {j} em estoque")

    print("\n1 - Comprar produto")
    print("2 - Sair")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "2":
        print("Até logo!")
        break
    elif opcao == "1":
        produto = input("Escolha um produto: ")
        quantidade = int(input("Quantos quer comprar? "))

        if produto in produtos:
            if quantidade <= produtos[produto]:
                produtos[produto] -= quantidade
                print(f"Compra realizada! Estoque restante de {produto}: {produtos[produto]}")
            else:
                print(f"Estoque insuficiente! Temos apenas {produtos[produto]} unidade(s).")
        else:
            print("Produto não encontrado!")
    else:
        print("Opção inválida!")
# %%
##3)#Carrinho de compras
#Crie uma lista vazia chamada carrinho. 
# Use um while para perguntar o nome de um produto ao usuário. 
# Se o produto for "sair", encerre. Caso contrário, adicione à lista. 
# No final, mostre todos os itens e a quantidade total.

print("============ CARRINHO =============")

lista = []

while True:
    print("Digite 1 - Para sair.")
    print("Digite 2 - Para adicionar um produto na lista.")
    try:
        opcao = int(input("Adicione o produto: "))
        if opcao == 1:
            print("Programa finalizado....")
            break
        else:
            produto = input("Digite o nome de um produto: ")
            lista.append(produto)
    except ValueError:
        print("Digite um numero...")

for i in lista:
    print(f"Produto -> {i}")

quantidade_produtos = len(lista)
if quantidade_produtos > 0:
    print(f"Temos {quantidade_produtos} produtos adicionados na lista!!!")
















# %%
