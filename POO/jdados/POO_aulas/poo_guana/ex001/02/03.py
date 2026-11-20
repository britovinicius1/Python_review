class ContaBancaria:
    """Cria uma conta bancaria e permite fazer saques e depositos"""

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"Conta {self.id} de {self.titular} | Saldo: R${self.saldo:,.2f}"

    def depositar(self, valor):
        if valor <= 0:
            print("O depósito precisa ser maior que zero.")
        else:
            self.saldo += valor
            print(f"Depósito de R${valor:,.2f} na conta {self.id}")

    def sacar(self, valor):
        if valor <= 0:
            print("O saque precisa ser maior que zero.")
        elif valor > self.saldo:
            print(f"Saque de R${valor:,.2f} negado! Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado na conta {self.id}")


c1 = ContaBancaria(id=112, nome="Gustavo", saldo=3000)
print(c1)
print(c1.__doc__)

c2 = ContaBancaria(id=114, nome="Joao", saldo=4000)
c2.sacar(2000000)

print("-----")
print(c2)