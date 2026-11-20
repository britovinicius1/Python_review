#Crie uma classe funcionario onde podemos cadastrar setor, nome e cargo
#crie também um método que permita ao funcionario apresentar.

#%%
class Funcionario:

    def __init__(self, setor, nome, cargo):

        self.setor = setor
        self.nome = nome 
        self.cargo = cargo

    def apresentar(self):
        return f"Oi, meu nome é  {self.nome}, sou da area de {self.setor} e tenho o cargo de {self.cargo} "


pessoa1 = Funcionario("RH", "Vinicius", "Analista de pessoas")
pessoa2 = Funcionario("TI", "Joao", "Data Analyst")


print(pessoa1.cargo)

print(pessoa2.nome)

pessoa1.apresentar()


# %%
#17) Crie a classe produto, onde  podemos cadastrar nome e preço. Crie
#também o metodo que mostre uma etiqueta de preço do produto


class Produto:
    def __init__(self, produto, preco):

        self.nome = produto
        self.preco = preco

    def mostrar_etiqueta(self):
        return f"O produto: {self.nome} tem preço ->>> {self.preco}"


produto1 = Produto("melao", 2.50)

produto2 = Produto("uva", 3)


produto1.mostrar_etiqueta()

# %%

#18)crie class churrasco, onde seja possivel informar
# quantas pessoas vao participar e mostre quantos de carne deve ser comprado
#custo total do churrasco e o preço por pessoa


class Churrasco:

    def __init__(self, pessoas, gramas):
        self.pessoas = pessoas
        self.gramas = gramas
        self.calculo_churrasco()

    def calculo_churrasco(self):
        self.gramas_carne = self.gramas * self.pessoas
        self.kgs_carne = self.gramas_carne / 1000
        self.custo_churrasco = self.kgs_carne * 55
        self.valor_individual = self.custo_churrasco / self.pessoas

    def __str__(self):
        return(
            f"Churrasco -> para {self.pessoas} pessoas \n"
            f"Qntd. carne -> {self.kgs_carne} kg \n"
            f"Total churrasco -> {self.custo_churrasco:,.2f}\n"
            f"Preço por pessoa -> {self.valor_individual:,.2f} por pessoa"
        )

# %%
Churras_turma_1 = Churrasco(25, 350)
Churras_turma_2= Churrasco(40, 600)



# %%
print(Churras_turma_1)
# %%
print(Churras_turma_2)
# %%
