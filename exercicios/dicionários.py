#%%
#090)
#Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
#Média > 7 aprovado

aluno_media = {}

aluno_media["Nome"] = input("Digite o nome do aluno:")
aluno_media["Media"] = float(input("Digita a média do aluno"))

if aluno_media["Media"] > 7:
    aluno_media["Situaçao"] = "Aprovado"
elif 5 <= aluno_media["Media"] < 7:
    aluno_media["Situaçao"] = "Recuperação"
else:
    aluno_media["Situaçao"] = "Aprovado"

for k,v in aluno_media.items():
    print(f"{k} é {v}")

#%%
#091)
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado.

#%%
#092)
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#+35 anos de contribuição -> aposenta;

from datetime import date

pessoa = {}

pessoa["Nome"] = str(input("Digite seu nome :"))
pessoa["ano_nascimento"] = int(input("Digite o ano que você nasceu:"))
pessoa["carteira"] = int(input("Digite o número da sua carteira de trabalho! (Se n possuir digite 0)"))
pessoa["Idadade"] = date.today().year - pessoa["ano_nascimento"]
if pessoa["carteira"] != 0:
    pessoa["Ano_contratacao"] = int(input("Ano de Contratação"))
    pessoa["Salario"] = float(input("Salario R$:"))

    pessoa["Apostendaoria"] = pessoa["Idadade"] + 35 - (date.today().year - pessoa["Ano_contratacao"])

for k,v in pessoa.items():
    print(f"{k} é igual a {v}")

# %%
#093)
#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato...

jogador = {}
gols = []
total = 0

jogador["Nome"] = str(input("Digite o nome do jogador: "))
jogador["Partidas"] = int(input("Quantas partidas ele jogou?"))

for i in range(0,jogador["Partidas"]):
    gol = int(input(f"Quantos gols o jogador fez na partida {i+1}?"))
    gols.append(gol)
    total += gol

jogador["Total"] = total

print("=-"*30)
print("-"*15, "ESTATISTICAS CAMPEONATO", "-"*15)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("=-"*30)
print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas")

for i,v in enumerate(gols):
    print(f"   => Na partida {i+1} ele fez {v} gols")

print(f"Foi um total de {jogador['Total']} gols no campeonato!!")

print("=-"*30)


    



# %%
