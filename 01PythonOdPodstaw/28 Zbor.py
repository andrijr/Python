import random
# zbór różni sie od kolekcji że nie są iterowane
# zbór nie koniecznie ma taką samą kolejność jaki był stworzony
# zbiór jest szybszy niż poprzednie kolekcje ( list tuple i string)
# elementy zbioru są zawsze unikalne


zbior = set()
print(zbior)
print(type(zbior))

slownik = {}
print(slownik)
print(type(slownik))

slownik = dict()
print(slownik)
print(type(slownik))


print('----')
zbior = {1, 2, 3, 4, 5, 6, 77, 88, 9, 10, 10, 88}
print(zbior)


print("wylosowanie 6 z 49 z urzyciem zbioru set")
zbior = set()
while len(zbior) < 10:
    zbior.add(random.randint(1, 49))
print(zbior)

lista = list(zbior)
print(lista)


print("wylosowanie 6 z 49 z urzyciem listy list")
lista = []
while len(lista) < 10:
    wylosowana = random.randint(1,49)
    if wylosowana in lista:
        continue
    lista.append(wylosowana)
print(lista)
