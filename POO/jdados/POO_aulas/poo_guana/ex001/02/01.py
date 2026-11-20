

# declaração da classe

class Gafanhoto:
    def __init__(self):             #metodo construtor --->> metodo na hr de instanciar
        ##atributos de instancia
        self.nome = ""
        self.idade = 0

    #metodos de instância
    def aniversario(self):
        self.idade = self.idade + 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"



#declaração do objeto
g1 = Gafanhoto() #chamada do metodo construtor
g1.nome = "Maria"
g1.idade = 17
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Joao" #(atributo)
g2.idade = 30
g1.aniversario() ###metodo

print(g2.mensagem())
print(g1.mensagem())

