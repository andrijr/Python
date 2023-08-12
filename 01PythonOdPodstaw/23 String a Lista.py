
lista = ["a", "b", "c"]
napis = "abc"
print(lista[1])
print(napis[1])
print("----")

for x in lista:
    print(x)
print("----")

for x in napis:
    print(x)
print("----")

# adres pamięci gdzie znajduję się lista
print(id(lista))
lista.append("d")
print(id(lista))

print(id(napis))
napis = napis + "d"
print(id(napis))
