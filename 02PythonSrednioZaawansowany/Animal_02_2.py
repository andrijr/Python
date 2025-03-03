from abc import ABC, abstractmethod

# jeżeli chcemy zaznaczyć że dana klasa jest abstrakcyjna wystarczy wpisać abc

class Animal(ABC):
    def __init__(self):
        raise Exception("Unable to create object of abstract class") # wyjątek klasy

    def printInformation(self): # metoda wirutalna
        pass

    @abstractmethod # wskazuję że metoda jest abstrakcyjna strikte wirtualna
    def giveVoice(self): # metoda wirtualna
        raise NotImplementedError()
        # metoda giveVoice staję się strikte wirtualna
        # w tym miejscu ta metoda staje się strikte wirtualna i że niema sensu a ma sens tylko w metodach pochodnych

class Marmal(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        print('go')

    def printInformation(self):
        print(self.name, self.age)
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


