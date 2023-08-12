import random
x = random.randint(1, 100)
print(x)

lista = [[1,2], [1,3], [1,4]]
for i in range(0, len(lista)):
    for j in range(0, len(lista[i])):
        print(lista[i][j])
print("-----")

for listaWewnetrzna in lista:
    for element in listaWewnetrzna:
        print(element)