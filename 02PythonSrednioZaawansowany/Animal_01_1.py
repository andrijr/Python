class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def printInformation(self): # metoda wirutalna
        print(self.name, self.age)

    def giveVoice(self): # metoda wirtualna
        raise NotImplementedError()
        # metoda giveVoice staję się strikte wirtualna
        # w tym miejscu ta metoda staje się że niema sensu a ma sens tylko w metodach pochodnych

class Marmal(Animal):
    def __init__(self, name, age):
        Animal.__init__(self,age, name)
    def run(self):
        print('go')

    def printInformation(self):
        Animal.printInformation()
        print("I am marmal")

class Cat(Marmal):
    def __init__(self, name, age, breed):
        Marmal.__init__(self, name, age)
        self.breed = breed

    def printInformation(self):
        Marmal.printInformation()
        print("I am Cat")

    def giveVoice(self):
        print('Miau')

class Dog(Marmal):
    def __init__(self, name, age, breed):
        Marmal.__init__(self, name, age)
        self.breed = breed

    def printInformation(self):
        Marmal.printInformation()
        print("I am Dog")

    def giveVoice(self):
        print('Hau Hau')


