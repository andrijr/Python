# Hermetyzacja jest to ukrywanie przed urzytkownikiem klasy pól dostępowych czyli selft.NazwaPola
# zamiast tego aby urzyć jakiegoś pola musimy urzyć metod dostępowych czyli metod które będą nadawać lub odczytywać wartośc pola

from Termometr_47_1 import *

temp = float(input("Podaj temperature: "))
unit = input("Podaj jednostkę 'C' dla celsjusza lub 'F' dla Faranhajta lub 'K' dla Kelwina ")

term = Termometr()
term.setTemperature(temp, unit)

while True:
    choice = int(input("Wpisz 0 jeżeli chcesz otrzymać temperaturę w jakeś jednosce lub 1 jeżeli chcesz nadac inną temperaturę \*9\* jeżeli chcesz zakończyć"))
    if choice == 9:
        break
    elif choice ==0:
        unit = input("Podaj jednostkę 'C' dla celsjusza lub 'F' dla Faranhajta lub 'K' dla Kelwina ")
        print(term.getTemperature(unit))
    elif choice == 1:
        temp = float(input("Podaj temperature: "))
        unit = input("Podaj jednostkę 'C' dla celsjusza lub 'F' dla Faranhajta lub 'K' dla Kelwina ")
        term.setTemperature(temp, unit)
    else:
        pass

