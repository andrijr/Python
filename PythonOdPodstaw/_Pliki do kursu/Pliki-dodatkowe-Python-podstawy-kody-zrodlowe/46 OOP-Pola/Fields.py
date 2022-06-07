class Car:
    def __init__(self,model,brand,number):
        self.colour = ""
        self.position = [0,0]
        self.model = model
        self.brand = brand
        self.vehicleRegistrationNumber = number
        self.speed = 0

    def printInformation(self):
        print("Mój kolor to: ",self.colour)
        print("Znajduję się w miejscu: ",self.position)
        print("Mój model: ",self.model)
        print("Moja marka: ",self.brand)
        print("Mój numer rejestracyjny: ",self.vehicleRegistrationNumber)
        print("Jadę z prędkością: ", self.speed)

    def increaseSpeed(self):
        self.speed += 2

    def getSpeed(self):
        return self.speed

myCar = Car("Astra","Opel","LUB 1234567")
anotherCar = Car("Lanos","Daewoo","WW 987654")
myCar.increaseSpeed()
myCar.printInformation()
anotherCar.printInformation()