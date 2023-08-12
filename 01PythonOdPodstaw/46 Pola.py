# Pola służą do tego aby określać pewne cechy obiektu.
# mamy klase samochody i zniej będziemy tworzyć objekty pojedynczych samochodów.
# clasa to coś w rodzaju wzorcu określonego objekut np. człowiek, kot, samochód.
# a np. kowalski to obiekt klasy człowiek.
# żeby utworzyć pole musimy posłużyć się metodą init, ta metoda wykonuję się wtedy kiedy tworzony jest obiekt
# metoda init wykonywana w czasie utworzenia objektu
# self oznacza że odwołujemym się do własnej klasy


class Car:
    def __init__(self, model, brand, number):
        self.colour = ""
        self.position = [0,0]
        self.model = model
        self.brand = brand
        self.vehicleRegistrationNumber = number
        self.speed = 0

    def printInformation(self):
        print("Mój kolor to", self.colour)
        print("Znajduję się w miejscu takiem", self.position)
        print("Mój model", self.model)
        print("Moja marka", self.brand)
        print("Mój numer rejestracyjny", self.vehicleRegistrationNumber)
        print("Jadę z prędkością", self.speed)

    def increaseSpeed(self):
        self.speed += 2

    def getSpeed(self):
        return self.speed



myCar = Car("Astra", "Opel","ABC123" )
myCar2 = Car(model="X", brand="Mercedes", number="XY123")

myCar.printInformation()
myCar.increaseSpeed()
print("----")
myCar.printInformation()