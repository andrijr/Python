
from Cat_48_1 import Cat
x = 3
y = 3

print(x==y)

kot1 = Cat(3, "biały", "dachowiec", "Mruczek")
kot2 = Cat(2, "niebieski", "brytyjski", "Sylwester")
kot3 = Cat(3, "biały", "dachowiec", "Mruczek")

# obiekty naszej klasy nie są porównywane po własnościach

print(kot1 == kot2)
print(kot2 == kot3)
print(kot1 == kot3)

print("----")
print(kot1)
kot1.getInformationAboutCat()
print(kot2)
kot2.getInformationAboutCat()
print(kot3)
kot3.getInformationAboutCat()

kot4 = kot1 # to jest ten sam kot to jest tylko inna nazwa dla tego samego kota to jest tylko nowy wskażnik na ten sam obszar pamięci
# to jest ten sam kot
print(kot4==kot1)

kot4.setName("Psotek")
kot1.getInformationAboutCat()
kot4.getInformationAboutCat()
print(kot1)
print(kot4)