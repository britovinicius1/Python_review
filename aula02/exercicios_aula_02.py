# 21)Conversor de temperatura
# Escreva um programa que converta a temperatura de celsius para farehint.
# Progama deve solicitar a temperatura em celsius e itulizando try-except
# Garantir que a entrada seja númerica, tratando qualquer valueerror.
#imprima o resultado convertido ou se jogar o erro enviar o erro.

#%%
print("Programa que transforma celsius em FH")
try:
    C = float(input("Digite um número em celsius"))
    F = (C * 9/5) + 32
    print(f"A temperatura em Fahrenheit é {F}°F")
except ValueError:
    print("Erro de valor, inseriur uma letra em vez de um número")


# %%
# 23) Calculadora simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

try:
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite um segundo número: "))
    operador = input("Digite um operador (+, -, *, /): ")
    resultado = None  # ← aqui

    if operador == '+':
        resultado = a + b
    elif operador == '-':
        resultado = a - b
    elif operador == '*':
        resultado = a * b
    elif operador == '/':
        if b == 0:
            print("Não dá pra dividir por zero!")
        else:
            resultado = a / b
    else:
        print("Operador inválido!")

    if resultado is not None:
        print(f"Resultado: {resultado}")

except ValueError:
    print("Insira um número..")

# %%
#24))Escreva um programa que solicite ao usuario digitar um número
# utilize try-except para assegurar que a entrada seja numérica e utilize
#if-else para classificar o número como positivo, negativo ou zero
#Adicionalmente indentifique se o numero é impar ou par.

try:
    numero = int(input("Digite um número para fazer o check"))
    if numero > 0:
        print("Número positivo")
    elif numero < 0:
        print("Numero negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Número par.")
    else:
        print("Numero impar")

except ValueError:
    print("Digite um número...")
# %%
