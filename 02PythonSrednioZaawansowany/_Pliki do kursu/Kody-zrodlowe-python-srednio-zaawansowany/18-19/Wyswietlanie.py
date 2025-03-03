class Obiekt:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    # def printMe(self):
    #     #return "Pierwsza zmienna: " + str(self.value1) + " " + "Druga zmienna: " + str(self.value2)
    #     return f"Pierwsza wartość: {self.value1} Druga wartość: {self.value2}"

    def __str__(self):
        return f"Pierwsza wartość: {self.value1} Druga wartość: {self.value2}"

    def __repr__(self):
        text = repr(Obiekt)
        return f"{text}\nPierwsza wartość: {self.value1} Druga wartość: {self.value2}"


obiekt = Obiekt(1,2)
print(repr(obiekt))