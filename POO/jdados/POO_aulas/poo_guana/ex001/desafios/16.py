#Crie uma classe funcionario onde podemos cadastrar setor, nome e cargo
#crie também um método que permita ao funcionario apresentar.

#%%

from rich import inspect
from rich import print

class Funcionario:

    #Atributos de classe

    empresa = "Red Bul"

    def __init__(self, setor, nome, cargo):

        self.setor = setor
        self.nome = nome 
        self.cargo = cargo

    def apresentar(self) -> str:
        return f"Oi, meu nome é {self.nome}, sou da area de {self.setor} e tenho o cargo de {self.cargo} na empresa {self.__class__.empresa}"


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

    def __init__(self, titulo, pessoas, gramas):
        self.pessoas = pessoas
        self.gramas = gramas
        self.titulo = titulo
        self.calculo_churrasco()

    def calculo_churrasco(self):
        self.gramas_carne = self.gramas * self.pessoas
        self.kgs_carne = self.gramas_carne / 1000
        self.custo_churrasco = self.kgs_carne * 82.5
        self.valor_individual = self.custo_churrasco / self.pessoas

    def __str__(self):
        return(
            f"--------------{self.titulo}--------------\n"
            f"Churrasco -> para {self.pessoas} pessoas \n"
            f"Qntd. carne -> {self.kgs_carne} kg \n"
            f"Total churrasco -> {self.custo_churrasco:,.2f}\n"
            f"Preço por pessoa -> {self.valor_individual:,.2f} por pessoa"
        )

# %%
Churras_turma_1 = Churrasco("Churras dos Amigos", 25, 600)
Churras_turma_2= Churrasco("festa dia 12", 40, 600)





# %%
print(Churras_turma_1)
# %%2
print(Churras_turma_2)
# %%
 #%%
from rich import print
from rich.panel import Panel


class Churrasco:
    consumo_padrao = 0.4   # kg por pessoa (chutei 400g)
    preco_kg = 55          # R$/kg (chutei o mesmo valor de antes)

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}"
        painel = Panel(conteudo, title=self.titulo)
        print(painel)


c1 = Churrasco(titulo="Churras dos Amigos", quant=15)
c1.analisar()




