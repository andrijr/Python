from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        raise Exception("Unable to create object of abstract class")
    def printInformation(self):
        pass

    @abstractmethod
    def giveVoice(self):
        raise NotImplementedError()

class Mammal(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print("go")

    def printInformation(self):
        print(self.name, self.age)
        Animal.printInformation(self)
        print("I am mammal")

class Cat(Mammal):
    def __init__(self,name,age,breed):
        Mammal.__init__(self,name,age)
        self.breed = breed

    def giveVoice(self):
        print("meow")

    def printInformation(self):
        Mammal.printInformation()
        print("I am cat")


class Dog(Mammal):
    def __init__(self, name, age, breed):
        Mammal.__init__(self, name, age)
        self.breed = breed

    def giveVoice(self):
        print("hau hau!")

    def printInformation(self):
        Mammal.printInformation()
        self.x = print("I am dog")
        