
class Obiekt:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def printMe(self):
        return 'pierwsze pole = ' + str(self.value1) + ' ' + 'druge pole = ' + str(self.value2)

    # po pierwsze polecane jest urzywanie formu czyli f
    def printMe2(self):
        return f"pierwsze pole =  {self.value1} druge pole = {self.value2}"

    # po drugie lepiej urzywać metody specjalnej def __str__(self): która jest wywoływana przy print
    def __str__(self):
        return f"pierwsze pole =  {self.value1} druge pole = {self.value2}"

    # nadpisanie metody repr
    def __repr__(self):
        tekst= repr(Obiekt)
        return tekst


obiekt = Obiekt(1,2)
print(obiekt)
print(obiekt.printMe())
print(obiekt.printMe2())

# metoda .__repr__() służy do wyświetlania pewnych informacji o obiekcie
print(obiekt.__repr__())
print(repr(obiekt))