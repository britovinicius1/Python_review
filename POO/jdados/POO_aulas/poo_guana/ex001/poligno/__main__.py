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

from rich import print, inspect
from poligno import *


def main():
    fig1 = Quadrado(12)
    fig2 = Circulo(12)

    fig1.area()
    fig1.perimetro()
    print("\n")
    fig2.area()
    fig2.perimetro()

    inspect(fig2)


if __name__ == "__main__":
    main()