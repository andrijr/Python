# wzorzec projektowy sposób definiowania klas w taki sposób aby były zgdone z naturalnym zachowaniem
# dziedziczenie wielokrotne jest to dziedziczenie po kilku klasach


# klasa która zachowuję informację tylko o metodach o zachowaniu a nie przechowuję informację o objękcie

class DuckBehaviour:
    def fly(self):
        print("Ja lecę")

    def say(self):
        print("Kwa Kwa")

    def go(self):
        print("Chodzę")

class Duck(DuckBehaviour):
    def __init__(self,age,breed):
        self.age = age
        self.breed = breed

class Toy:
    def __init__(self,color, material):
        self.color = color
        self.material = material

class DuckToy(Toy, DuckBehaviour):
    pass

    # def fly(self):
    #     print("I am fly")
    # def say(self):
    #     print("kwa kwa")
    # def go(self):
    #     print("go go")

#DRY = Do not Reply Yourself
