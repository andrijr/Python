from Numbers import Numbers
from Cars import Car

liczby1 = Numbers([])
liczby1.addNumberToList(3)
liczby1.addNumberToList(5)
liczby1.addNumberToList(7)
liczby1.addNumberToList(1)
liczby1.addNumberToList(2)

liczby2 = Numbers([])
liczby2.addNumberToList(10)
liczby2.addNumberToList(20)
liczby2.addNumberToList(30)

print(liczby1.numbers)
print(liczby1.sumNumbers())
print(liczby2.numbers)
print(liczby2.sumNumbers())

print(Numbers.numbersSum)

# print(liczby.productNumbers())
#
# print(Numbers.subtractNumbers(3,5))
# Numbers.printInformationAboutMe()

# samochod1 = Car(Car,"inna")
# samochod2 = Car(Car,"inna")
# samochod3 = Car(Car,"inna")
# samochod4 = Car(Car,"inna")
#
# print(samochod3.howManyCars)