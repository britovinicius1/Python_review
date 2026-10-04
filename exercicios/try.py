#Reescreva a função leiaInt() que fizemos no desafio 104,
#  incluindo agora a possibilidade da digitação de um número 
# de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() 
# com a mesma funcionalidade./
#%%
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except ValueError:
            print("Você digitou errado! Digite um número inteiro.")


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("Você digitou errado! Digite um número inteiro.")
            continue
        except KeyboardInterrupt:
            print("O usuario preferiu nao digitar esse resultado")
            return 0
        else:
            return n

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")
