tupla = (1,2,3)
lista = [4,5,6]
string = "abc"

lista2 = [12, 33, tupla, "abc"]
tupla2 = ("Tu jest lista:",lista,lista2)

print(tupla[1])
print(lista[2])
print(string[0])
print(lista2)
print(tupla2)

print(lista2[1:])
print(string[1:])

print(lista2[-2::-2])
print(tupla[::-1])
print(string[::-1])

#  [start:stop:step]

listaZnakow = list(string)
listaZnakow[1] = 'd'
string = "".join(listaZnakow)
print(string)