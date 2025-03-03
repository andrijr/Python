# pola klasowe
# metody klasowe
# metody statyczne

from Cars_07_2 import Car2
from Numbers_06_2 import Numbers

samochod1 = Car2(Car2,"inna")
samochod2 = Car2(Car2,"inna")
samochod3 = Car2(Car2,"inna")
samochod4 = Car2(Car2,"inna")

print(Car2.howManyCars)


print("----")
liczby1 = Numbers([])
liczby1.addNumbersToList(3)
liczby1.addNumbersToList(5)
liczby1.addNumbersToList(7)
liczby1.addNumbersToList(1)
liczby1.addNumbersToList(2)

print(liczby1.numbers)
print(liczby1.sumNumbers())
print(liczby1.numbersSum)

print("----")
liczby2 = Numbers([])
liczby2.addNumbersToList(10)
liczby2.addNumbersToList(20)
liczby2.addNumbersToList(30)

print(liczby2.numbers)
print(liczby2.sumNumbers())
print(liczby2.numbersSum)

print(Numbers.numbersSum)