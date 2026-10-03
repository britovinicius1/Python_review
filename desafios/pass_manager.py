#Crie um programa em Python, via linha de comando, que funcione como um cofre de notas criptografadas. Requisitos:
def adicionar():
    titulo = str(input("Titulo:"))
    password = input("Password:")

    with open("notas.txt", 'a') as f:
        f.write(f"{titulo}" + " | " + f"{password}" + "\n")

def visualizar():
    with open("notas.txt", "r") as f:
        linhas_lista = f.readlines()

        if not linhas_lista:
            print("Nenhuma senha salva...")
        else:
            print("Senhas salvas:")
            for i,linha in enumerate(linhas_lista):
                titulo,senha = linha.split("|")
                print(f"{i+1} - {titulo}")
        
    print("="*45)

def ler_nota():
    nota_escolhida = int(input("Qual nota você quer ler? [numero]"))
   
    with open("notas.txt", 'r') as f:
        for pos,linha in enumerate(f):
            titulo,senha = linha.split("|")
            if (pos+1) == nota_escolhida:
                print(f"Titulo: {titulo}\nPassword:{senha}")

def deletar_nota():
    with open("notas.txt", "r") as f:
        linhas = f.readlines()          # lista com todas as linhas

    visualizar()
    indice = int(input("Qual nota apagar? "))

    linhas.pop(indice-1)                  # remove só aquela linha

    with open("notas.txt", "w") as f:
        f.writelines(linhas) 


## Programa principal ##
print("="*20, "Caderno gerenciador de senhas", "="*20)
while True:
    opcao = input("O que você quer fazer? \n"
    "(1) - Adicionar\n" \
    "(2) - Titulos salvos\n" \
    "(3) - Ler uma nota especifica \n"
    "(4) - Apagar uma nota\n" \
    "q -> sair do programa\n")

    if opcao == 'q':
        print("Saindo do programa..")
        break
    elif opcao == '1':
        adicionar()
    elif opcao == '2':
        visualizar()
    elif opcao == '3':
        ler_nota()
    elif opcao == '4':
        deletar_nota()
    else:
        print("Digite uma opção valida...")
    


# %%
