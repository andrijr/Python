#I sposób - dziesięć dziesiątek
lista = []
for i in range(10):
    lista.append(10)
print(lista)

#II sposób
lista2 = [10]*10
print(lista2)

napis = "abc" * 7
print(napis)

#III sposób - Wyrażenia listowe
lista3 = [10 for i in range(10)]
print(lista3)

#lista = [wyrażenie for element in kolekcja]

lista4 = [litera for litera in "Jakiś napis"]
print(lista4)

lista5 = [int(znak) for znak in "0123456"]
print(lista5)

x, y = [int(liczba) for liczba in input("Podaj dwie liczby: ").split()]
print(x*y)