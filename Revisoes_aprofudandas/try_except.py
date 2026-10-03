#%%
try:
    a = int(input("Numerador:"))
    b = int(input("Denominador:"))
    r = a / b
except Exception as erro:
    print(f"Infelizmente deu um erro... o problema encontrado foi -> {erro}")
else:
    print(f"o resultado é {r}")
finally:
    print("Volte sempre.. Mto obrigado!!")
# %%
try:
    a = int(input("Numerador:"))
    b = int(input("Denominador:"))
    r = a / b
except (ValueError, TypeError):
    print(f"Tivemos um problema com os tipos de dados que você digitou")
except ZeroDivisionError:
    print(f"Não é possivel dividir por zero")
else:
    print(f"o resultado é {r}")
finally:          
    print("Volte sempre.. Mto obrigado!!")

#%%
#Exceção -> objeto que representa um erro que ocorreu ao executar o programa
#suspeita que pode ocorrer um erro pra precaver e explodir o erro na hora de usar
# o programa trava..
#com try o programa continua e não quebra

try:
    n1 = int(input("Digite um numero"))
    n2 = int(input("Digite um numero"))
    r = round(n1/n2, 2)
except ZeroDivisionError:
    print(f"Não é possivel dividir por zero!!")
else:
    print(f"Resultado {r}")

# %%
def div(k,j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input("Digite um numero"))
            n2 = int(input("Digite um numero"))
            break
        except ValueError:
            print(f"Ocorreu um erro ao ler o valor. Tente novamente!")
    
    try:
        r = div(n1 , n2)
    except ZeroDivisionError:
        print(f"Não é possivel dividir por zero!")
    except:
        print(f"Ocorreu um erro desconhecido!!..")
    else:
        print(f"O resultado é {r}")
    finally:
        print("Fim do calculo!! (Sempre será executado, se der erro ou não!)")
# %%
from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input("Digite um número positivo:"))
        if num < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print(f"Foi fornecido um número negativo!")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print("Fim de cálculo!!")
# %%
