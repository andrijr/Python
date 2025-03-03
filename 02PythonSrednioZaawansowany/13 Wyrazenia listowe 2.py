
# wyrażenia listowe
# [wyrażenie for element in kolekcja if warunek]

kwadraty = [abs(x*x+3*x-5) for x in range(10)]
print(kwadraty)

kwadraty2 = []
for x in range(10):
    kwadraty2.append(abs(x*x+3*x-5))
print(kwadraty2)

zbior = set(kwadraty)
print(zbior)


zbior2 = {abs(x*x+3*x-5) for x in range(10)}
print(zbior2)

slownik = {x: x*x for x in range(11)}
print(slownik)

lista = [ [i] for i in range(11)]
print(lista)

lista2 = [ [x for x in range(3)] for y in range(11)]
print(lista2)

lista3 = [x.lower() for x in 'aAbCdE']
print(lista3)

lista4 = [x * y for (x,y) in ([1,2], [3,4])]
print(lista4)

lista5 = [x * y for x,y in ([a,a+1] for a in range(19))]
print(lista5)

lista6 = [[x * y, (x+1)*(y+1)] for x,y in ([a,a+1] for a in range(19))]
print(lista6)

lista7 = [[x * y, (x+1)*(y+1)] * 3 for x,y in ([a,a+1] for a in range(6))]
print(lista7)