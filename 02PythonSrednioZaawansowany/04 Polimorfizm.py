from  Duck_04_1 import *

# mechanizm polimorfizmu pozwala urzyć tej samej metody niezależnie od typu pozwala na uruchomienie tego samego kodu.
# poliformizm można osiągnąć z dziedziczeniem lub dziedziczeniem wielokrotym lub bez dziedziczenia


kaczka = Duck(3,"aaa")
zabawka = DuckToy("zielony","plastik")

lista = [kaczka, zabawka, kaczka, zabawka, Robot("Wyszukiwarka")]
lista[0].say()



lista = [kaczka, zabawka, kaczka, zabawka, Robot("Android")]

print("Sposób pierwszy")
for obiekt in lista:
    if hasattr(obiekt, "fly") and hasattr(obiekt, "say"):
        obiekt.say()
        obiekt.fly()
    else:
        print("Obiekt",obiekt,"nie posiada metody fly")

print("Sposób drugi")
for obiekt in lista:
    try:
        obiekt.say()
        obiekt.fly()
    except AttributeError:
        print("Obiekt", obiekt, "nie posiada jednej z wymaganych metod")

lista = ['a', 'b', 'c']
napis = "abc"
liczba = 3
print(len(lista))
print(len(napis))
print(lista.__len__())
print(napis.__len__())

def read(parametr):
    print(parametr)

read(napis)
read(lista)
read(liczba)
