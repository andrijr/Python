
lista1 = [1,2,3]
lista2 = [1,2,3]

print(lista1 == lista2) # True sprawdzamy cz różne listy obiekty są sobie równe
print(lista1 is lista2) # False # sprawdzamy czy to ta sama lista ten sam obiekt z inną nazwą

lista3 = lista2 # tworzenie drugej nazwy do tego samego obiektu
print(lista2 is lista3) # True


lista2.append(4)
print(lista2)
print(lista3)

lista4 = lista2[:] # utworzenie nowej listy na podstawie innej listy
lista2.append(5)
print(lista2,lista3, lista4)

class Obiekt:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def __eq__(self, other): # metoda specjalna do umożliwienia sprawdzania czy obiekty maą takie same wartości
        return self.value1 == other.value1 and self.value2 == other.value2

obiekt1 = Obiekt(1,2)
obiekt2 = Obiekt(1,2)

print("---")
print(obiekt1 == obiekt2) # False # są różne obiekty z tymi samymi wartościami a mimo to jest False
print(obiekt1 is obiekt2) # False # bo to są różne obiekty
print(id(obiekt1) == id(obiekt2)) # False # is oznacza id = id

print(obiekt1 == obiekt2) # True po urzyciu specjalnej metoyd def __eq__(self, other):

print(obiekt1.value1 == obiekt2.value1 and obiekt1.value2 == obiekt2.value2)

print("---")
print(obiekt1 == obiekt2) # przeciążenie operatora jest to skrót od takiego zapisu obiekt1.__eq__(obiekt2)
print(obiekt1.__eq__(obiekt2)) # przeciążenie operatora

