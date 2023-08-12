import random

wylosowana = random.randint(1, 1000)
print(wylosowana)

lista = []
for x in range(0,6):
    wylosowana = random.randint(1,49)
    if wylosowana in lista:
        continue
    lista.append(wylosowana)
print(lista)


lista = []
while len(lista) < 6:
    wylosowana = random.randint(1,49)
    if wylosowana in lista:
        continue
    lista.append(wylosowana)
print(lista)