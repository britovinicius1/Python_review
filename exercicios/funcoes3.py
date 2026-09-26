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
##102)