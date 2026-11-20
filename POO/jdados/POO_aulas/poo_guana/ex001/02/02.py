class Gafanhoto:
    """
    Essa classe cria um ganhafoto que tem nome e idade

    Para criar uma pessoa, use 
    variavel = Gafonhoto(none,idade)
    
    """

    def __init__(self,n="", i=0):             
       
        self.nome = n
        self.idade = i

    #metodos de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} e tem a idade de {self.idade} anos"

    


g1 = Gafanhoto(n="Maria", i=18)


print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

print(int.__doc__)