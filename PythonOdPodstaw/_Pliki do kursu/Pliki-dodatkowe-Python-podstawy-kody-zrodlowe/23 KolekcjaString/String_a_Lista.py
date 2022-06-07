# lista = ["a","b","c"]
# napis = "abc"
#
# print(lista[1])
# print(napis[1])
#
# lista.append("d")
# napis = napis + "d"
#
# for element in napis:
#     print(element)

lista = ["a","b","c"]
napis = "abc"

print(lista)
print(id(lista))
lista.append("d")
print(lista)
print(id(lista))

print()
print("---")

print(napis)
print(id(napis))
napis = napis + "d"
print(napis)
print(id(napis))