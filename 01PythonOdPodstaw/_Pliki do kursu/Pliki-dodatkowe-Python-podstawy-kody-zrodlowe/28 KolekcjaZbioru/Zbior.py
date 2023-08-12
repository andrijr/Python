import random

# lista = []
# while len(lista) < 30000:
#     wylosowana = random.randint(1,1000000)
#     if wylosowana in lista:
#         continue
#     lista.append(wylosowana)
#
# print(lista)

zbior = set()
while len(zbior) < 100000:
    zbior.add(random.randint(1,1000000))

lista = list(zbior)
print(lista)