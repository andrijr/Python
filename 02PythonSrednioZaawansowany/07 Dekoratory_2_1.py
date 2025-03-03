# klasa opróc metod powinna posiadać pola clasowe
# do pól klasowych możemy się odwoływać przy pomocy class metod

from Cars_07_1 import Car

samochod = Car("inna")

# zarówno objekt i klasa zawiera informacje o polu klasy
print(samochod.howManyCars)
print(Car.howManyCars)

samochod.addCar()

print(samochod.howManyCars)
print(Car.howManyCars)

print("----")
# to są dwa różne pola
samochod.howManyCars = 10
print(samochod.howManyCars)
print(Car.howManyCars)

# dodaję tylko do clasy bo pole objektu jest 10
samochod.addCar()
print(samochod.howManyCars)
print(Car.howManyCars)

# dodaję i do clasy do pola i do objektu
Car.addCar()
print(samochod.howManyCars)
print(Car.howManyCars)

# dodajemy do innego objektu a wzrasta w klasie.
innySamochod = Car("NowySamochod")
innySamochod.addCar()
print(samochod.howManyCars)
print(Car.howManyCars)

