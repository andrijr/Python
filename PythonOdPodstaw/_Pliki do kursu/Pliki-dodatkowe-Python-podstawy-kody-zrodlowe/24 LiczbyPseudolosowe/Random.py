import random

lista = []
while len(lista) < 6:
    wylosowana = random.randint(1,49)
    if wylosowana in lista:
        continue
    lista.append(wylosowana)

print(lista)