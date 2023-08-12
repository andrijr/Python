class Cat: # klasa Cat
    def __init__(self, age, hair, breed, name): # metoda init
        self.age = age
        self.hair = hair
        self.breed = breed
        self.name = name

    def getInformationAboutCat(self):
        print( self.age, self.hair, self.breed, self.name)

    def mow(self):
        print("miau")

    def setName(self, name):
        self.name = name



