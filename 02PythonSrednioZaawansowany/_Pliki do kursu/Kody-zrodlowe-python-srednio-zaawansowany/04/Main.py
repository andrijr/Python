from Duck import *

kaczka = Duck(3,"aaa")
zabawka = DuckToy("zielony","plastik")

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

lista = ["a", "b", "c"]
napis = "abc"
liczba = 3
print(lista.__len__())
print(napis.__len__())
#print(len(liczba))

def read(parametr):
    print(parametr)

read(lista)
read(napis)
read(liczba)