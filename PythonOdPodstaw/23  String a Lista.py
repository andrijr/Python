lista = ["a", "b", "c"]
napis = "abc"
print(lista[1])
print(napis[1])
print("")

lista.append("d")
napis = napis + "d"

for i in lista:
    print(i)

for i in napis:
    print(i)

print("")

print(id(lista))
lista.append("e")
print(id(lista))

print(id(napis))
napis = napis + "e"
print(id(napis))