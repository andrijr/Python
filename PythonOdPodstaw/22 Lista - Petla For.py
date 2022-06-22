lista = [1, 5, 7, 9]
print(lista[len(lista)-1])
print(lista[-1])
lista.reverse()
print(lista)

lista = []
liczba = int(input("podaj liczbę: "))
while liczba >0:
    lista.append(liczba)
    liczba = int(input("Podaj kolejną liczbę: "))

suma = 0
for wartosc in lista:
    suma += wartosc
print("suma", suma)
print("średnia aretmetyczna", suma/len(lista))

