


lista = []
liczba = int(input("Podaj wartość: "))
while liczba > 0:
    lista.append(liczba)
    liczba = int(input("Podaj wartość: "))
print(lista)

suma = 0
for wartosc in lista:
    suma += wartosc
print(suma/len(lista))

print(lista[len(lista)-1])
print(lista[-1])
print(lista[-2])

lista.reverse()
print(lista)

