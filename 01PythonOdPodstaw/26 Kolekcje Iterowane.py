# objekty typu kolekcje
tupla = tuple()
tupla = ()

lita = list()
lista = []

tupla = ( 1, 2, 3)
lista = [3, 4, 5]
string = "abc"

print(tupla)
print(lista)
print(string)

print(tupla[1])
print(lista[1])
print(string[1])

lista2 = [1, 2, lista, 4, 5, tupla, "abc", 8, 9, 10]
print(lista2)
tuple2 = (1, 2, lista, 4, 5, tupla, "abc", 8, 9, 10)
print(tuple2)
print("----")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [ start : koniec : krok ]
print(lista[2:8], "lista od 3 do 8 ")
print(lista[2:8:2], "lista od 3 do 8 z krokiem 2 czyli 3 5 7 ")
print(lista[2], "trzeci element listy")
print(lista[:2], "lista od początku do  2 elementu")
print(lista[2:], "listata od 3 elementu do końca")
print(lista[:-2], "lista od początku bez 2 ostatnich elementów")
print(lista[-2:], "lista z dwoma ostatnimi elementami")
print(lista[::2], "lista z krokiem co 2 elementy od początku yświetla 1 3 5 itd")
print(lista[::-2], "lista z krokiem co 2 elementy od końca wyświetla 10 8 6  itd")
print(lista[::-1], "lista odwrócona")
print(lista[1:7], "lista od 2 od 7 elementu")
print(lista[1:-1], "lista bez pierwszego i ostatniego elementu")



# konwersja
string = "tekst"
listaZTekstu = list(string)
listaZTekstu = list("tekst xx")
print(listaZTekstu)

lista = listaZTekstu
string = ''.join(lista)
print(string)
print("----")

tupla = (1,2,3)
tuple2 = tupla
print(tupla)
listaZTuple = list(tupla)
print(listaZTuple)

tupleZListy = tuple(lista)
print(type(tupleZListy))


print(string[::-1])
