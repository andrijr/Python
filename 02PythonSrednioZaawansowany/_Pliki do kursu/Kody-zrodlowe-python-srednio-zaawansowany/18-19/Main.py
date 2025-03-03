lista1 = [1,2,3]
lista2 = [1,2,3]

lista3 = lista1[:]
lista3.append(4)

print(lista1 is lista3)


class Obiekt:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def __eq__(self, other):
        return self.value1 == other.value1 and self.value2 == other.value2

obiekt1 = Obiekt(1,2)
obiekt2 = Obiekt(1,2)

print()
print(obiekt1 == obiekt2)