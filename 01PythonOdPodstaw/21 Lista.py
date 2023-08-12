
lista = list()
print(lista)

lista = []
print(lista)

lista.append(3)
lista.append(5.2)
lista.append("Tekst")
print(lista)
print(lista[2])
print(len(lista))

lista[2] = 123
print(lista)
lista.remove(lista[2])
print(lista)
lista.append(3)
lista.append(3)
print(lista)
lista.remove(3)
print(lista)
lista.remove(3)

print(lista)
print(id(lista))
lista = lista + [4]
print(lista)
print(id(lista))