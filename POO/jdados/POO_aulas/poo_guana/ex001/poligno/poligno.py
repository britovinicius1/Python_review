#23) Implemente o seguinte diagrama de classe:

#classe poligno
#subclasse -> qtde de lados
#perimetri e area() ------> metodos abstratos


#subclasses

#quadrado
# - lado
# perimetro
# area

#circulo
# - raio
# - perimetro
# - area

# herança -> quadrado e circulo é um poligno

from abc import ABC, abstractmethod

PI = 3.14

class Poligno(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligno):

    def __init__(self, ladosv1):
        super().__init__(ladosv1)
     
    def perimetro(self) -> float:
        perimetro = 2 * self.qtd_lados * 4
        print(f"O perimetro do quadrado é: {perimetro}")

    def area(self) -> float:
        area = self.qtd_lados * self.qtd_lados
        print(f"A area do quadrado é: {area}")


class Circulo(Poligno):

    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> float:
        print(f"O perimetro do circulo é: {self.raio * PI}")

    def area(self) -> float:
        calculo_area = PI * (self.raio ** 2)
        print(f"A area do circulo é: {calculo_area}")
         

        
