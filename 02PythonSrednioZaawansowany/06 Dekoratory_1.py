# Dzięki nim możemy tworzyć i zaznaczać metody którę są klasą albo jakąs statyczną
# To znaczy że jakaś metoda może działać bez intstancji to znaczy bez obiektu
#

from Numbers_06_1 import Numbers

liczby = Numbers()
liczby.addNumbersToList(3)
liczby.addNumbersToList(5)
liczby.addNumbersToList(7)
liczby.addNumbersToList(1)
liczby.addNumbersToList(2)

print(liczby.sumNumbers())
print(liczby.prouctNumbers())

# metodę substracNumbers moge wywołac bez instancji bez utworzonego obiekut poniewaz do tej metody jest dekorator
# dzięki dekoratorowi @staticmethod możemy tworzyć metody nie wymagające objektów czyli instancji
print(Numbers.substractNumbers(3,1))


# dzięki dekoratorowi @classmethod i cls możemy się odwoływać do nazwy klasy
Numbers.printInformationAboutMe()