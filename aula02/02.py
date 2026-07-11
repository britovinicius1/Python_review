# 1. Inteiros (int)
# Métodos e operações:
# + (adição)
# - (subtração)
# * (multiplicação)
# // (divisão inteira)
# % (módulo - resto da divisão)

# 2. Números de Ponto Flutuante (float)
# Métodos e operações:
# + (adição)
# - (subtração)
# * (multiplicação)
# / (divisão)
# ** (potenciação)

# Métodos e operações:
# .upper() (converte para maiúsculas)
# .lower() (converte para minúsculas)
# .strip() (remove espaços em branco no início e no final)
# .split(sep) (divide a string em uma lista, utilizando sep como delimitador)
# + (concatenação de strings)

# 4. Booleanos (bool)
# Operações lógicas:
# and (E lógico)
# or (OU lógico)
# not (NÃO lógico)
# == (igualdade)
# != (diferença)

# ----------------------

#%%
nome = "Vinicius"
eamil = "brito.vini@outlook.com"
print(nome.upper())
print(nome.lower())
print(nome.strip())
print(eamil.split("@"))
#%%
data_usuario = input("Insira uma data no formato dd/mm/aaaa:")
lista = data_formatada = data_usuario.split("/")
dia_data_usuario = data_formatada[0]
mes_data_usuario = data_formatada[1]
ano_data_usuario = data_formatada[2]

print(f"Com a data digitada temos o dia {dia_data_usuario}, do mes {mes_data_usuario} e o ano {ano_data_usuario}")

# %%
## TypeError, Type Check e Type Conversion em Python
# se??? acontecer tal coisa? ai vc coloca pra ele testar
try:
    a = int(input("Digite o numero 1:"))
    b = int(input("Digite o numero 2:"))
    resultado = a / b
    print(resultado)
except ZeroDivisionError:
    print("Erro por divisão de zero")
except KeyboardInterrupt:
    print("Acho que você nao inseriu um nome")

# %%
try:
    resultado = len("aaa")
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("Caso ocorreu bem, vai aparecer esse else.")
finally:
    print("Independente de o que aconteceu faz isso também!!!")
# %%
#ele checa a variavel se é de um tipo;
numero = input("Insira um númmero")

if isinstance(numero,int):
    print("A variavel é um inteiro")
else:
    print("A variavel não é um inteiro")

# %%
#o If é checea isso se nao faz aquilo

idade = 15
if idade < 18:
    print("Não pode dirigir")
elif idade == 18:
    print("Pode tirar a carteira esse ano")
else:
    print("Pode dirigir!!")

# %%
