class Cat:
    def __init__(self,age,hair,breed,name):
        self.age = age
        self.hair = hair
        self.breed = breed
        self.name = name
        
    def printInformationAboutCat(self):
        print(self.age, self.hair, self.breed, self.name)
        
    def meow(self):
        print("Meow")

    def setName(self, name):
        self.name = name