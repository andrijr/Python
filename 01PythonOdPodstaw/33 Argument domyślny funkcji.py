def suma_trzech (a, b, c):
    return a + b + c


def suma_dwoch (a, b):
    return a + b


print(suma_dwoch(2, 3))
print(suma_trzech(4, 5, 6))



def suma (listaLiczb: list):
    wynik = 0
    for x in listaLiczb:
        wynik += x
    return wynik


x = float(input("podaj liczbę aby zakończyć podaj 0: "))
lista = []
while x != 0:
    lista.append(x)
    x = float(input("podaj liczbę aby zakończyć podaj 0: "))
print(suma(lista))



def sredniaAretmetyczna (listaLiczb: list):
    wynik = 0
    licznik = 0
    for x in listaLiczb:
        wynik += x
        licznik += 1
    return wynik / licznik

lista2 = [1, 2, 3 ,4 ,6 ,7 ,8 ,9, 10 ]
print(sredniaAretmetyczna(lista2))
