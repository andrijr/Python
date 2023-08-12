class Animal:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def printInformation(self):
        print(self.age)
        print(self.name)

    def giveTheVoice(self):
        print("voice")


class Mammal(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age, name)

    def go(self):
        print("go go go")

    def printInformation(self):
        Animal.printInformation(self)
        print("I am mammal")


class Cat(Mammal):
    def __init__(self, age, name, breed):
        Mammal.__init__(self, age, name)
        self.breed = breed

    def giveTheVoice(self):
        print("meow!")

    def printInformation(self):
        Mammal.printInformation(self)
        print(self.breed)
        print("I am cat")


class Dog(Mammal):
    def __init__(self, age, name, breed):
        Mammal.__init__(self, age, name)
        self.breed = breed