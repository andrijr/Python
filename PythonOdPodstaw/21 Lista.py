# kolekcje
# lista

lista = []

lista.append(4)
lista.append("tekst")
lista.append(True)
print(lista)
lista[1] = "ok"
print(len(lista))
print(lista)
lista.remove(lista[2])
print(lista)
lista.remove("ok")
print(lista)