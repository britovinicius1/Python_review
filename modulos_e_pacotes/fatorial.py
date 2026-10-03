
#%%
### MODULOS ##
## organização das funções em outro arquivo de acordo com a funcionalidade

# Vantagens -> Organização do código - divide o código em menores
# Facilidade de manutenção -> atualiza de forma facil
# Oculta o código detalhda -> nao preciso me preocupar como é feito
# Reutilização em outro projetos.

##from uteis import fatorial,dobro (não é tao recomendada - pode dar conflito - vale sempre a ultima importada)
## exemplo from random import randit - primeiro é o modulo e o segundo é a função

from uteis import numeros

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {numeros.dobro(num)}")
print(f"O triplo de {num} é {numeros.triplo(num)}")


# %%

## PACOTES ##
#ex: pacote uteis
# PACOTE(BIBLIOTECA) -> pasta que contem modulos, separa por assunto
#toda pastsa criada dentro é um pacote, e ali cria outra pasta q é um modulo;
# __init__.py (dentro de cada pasta) ->> passa pro python que a pasta é um pacote
#roda o arquivo automaticamente quando dar o import

