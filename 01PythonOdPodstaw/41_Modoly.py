#import Modoly_41_1
from Modoly_41_1 import *

lista = []

try:
    liczba = int(input("Podaj liczbę całkowitą: "))
except:
    print("to nie jest poprawna liczba")
while liczba != 0:
    lista.append(liczba)
    try:
        liczba = int(input("Podaj liczbę całkowitą: "))
    except:
        print("to nie jest poprawna liczba")

print(dodawanie(lista))