import Tetragon_51_1
from Tetragon_51_1 import *

kwadrat = Tetragon_51_1.Square(5)
prostokat = Tetragon_51_1.Rectagle(10,16)

lista = [prostokat, kwadrat]

print(kwadrat.area())
print(kwadrat.perimetr())

print(prostokat.area())
print(prostokat.perimetr())

for figura in lista:
    print(figura.area())
    print(figura.perimetr())
