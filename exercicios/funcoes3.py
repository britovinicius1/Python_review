#%%
#101)
#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
# , retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto(nascimento: int) -> str:

    """
    Função que calcula a posibilidade de voto

    Args:
        nascimento: Ano de nascimento
    Return:
        Retorna a possibilidade do voto
    """

    ano_atual = datetime.now().year
    idade = ano_atual - nascimento

    if idade < 16:
        faixa = f"Você tem {idade} anos.\nVoto Negado!!!"

    elif (16 <= idade < 18) or idade > 69:
        faixa = f"Você tem {idade} anos.\nVoto Opcional!!"
    else:
        faixa = f"Você tem {idade} anos.\nVoto Obrigatório!!"

    return faixa

print("-"*20,"Inicio do programa", "-"*20)
while True:
    print("="*20)
    ano_nascimento = int(input("Em que ano você nasceu? "))
    if ano_nascimento == 999:
        print("Fim do programa!!")
        break
    else:
        print(voto(ano_nascimento))
        
# %%
##102)Crie um programa que tenha uma função fatorial() 
# que receba dois parâmetros: 
# o primeiro que indique o número a calcular e o outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou 
# não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de um número n.
    """

    f = 1
    for i in range(n, 0, -1):
        
        if show:
            print(i, end="")
            if i > 1:
                print(f" x ", end="")
            else:
                print(" = ", end="")    
        f *= i
    return f

print(fatorial(5, show=True))

# %%
#103)
#Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou.

#O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador="<desconhecido>", gol=0):
    print(f"O jogador {jogador} fez {gol} gol(s) no campeonato!!")


## Programa ##
n = str(input("Nome do Jogador:"))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == "":
    ficha(gol=n)
else:
    ficha(n,g)

# %%
#104)
#Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante à função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico.

