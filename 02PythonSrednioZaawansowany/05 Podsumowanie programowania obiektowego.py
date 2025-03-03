# programowanie obiektowe to jest pewny styl programowania zoorintowany obiektowo

# 1. Abstrakcja
# budowanie programów przyjaznych do naszego zrozumienia
# mówimy o uprzedmiotowieniu że mówimy o jakichś obiektach
# uogolnienie pewnego problemu odseparowanie pewnego problemu od jego implementacji
# Przykład: liczba naturalna 5

# pewną abstrakcją morze być dowolny element zbioru liczb naturalnych
# większą abstrakcją będzie zbiór liczb naturalnych
# większą abstrakcją będzie zbiór liczb rzeczywistych


# 2. Hermetyzacja (Enkapsulacja)
# jest to proces ukrywania pewnych danych
# ukrywanie zmiennych żeby nie byli dostępne poza klasą
# ukrywanie jakiejś metody do pliku
# hermetyzacja ukrywa implementacje

# 3. Dziedziczenie
# Dziedziczenie polega na przejmowaniu cech klasy bazowej przez klasę pochodną

# 4. Polimorfizm
# Mechanizm pozwalanjący na operowanie na wielu różnych obiektach w ten sam sposób



# istnieje możliwość ukrycia pewnej zmiennej
class Temp:
    def __init__(self):
        self.a = 3
        self.__a = 5
    def printMe(self):
        print(self.a)
        print(self.__a)


obiekt = Temp()
obiekt.printMe()
print(obiekt.a) # print zmiennej a
## print(obiekt.__a) # print zmiennej a nie jest możliwy bo zmienna ukryta
