#lista = [wyrażenie for element in kolekcja]

kwadraty = [abs(x*x+3*x-5) for x in range(10)]
print(kwadraty)

# squares = []
# for x in range(10):
#     squares.append(x*x+3*x+5)
# print(squares)

kwadraty = {abs(x*x+3*x-5) for x in range(10)}
print(kwadraty)

slownik = {x: x**3 for x in range(11)}
print(slownik)
print()

lista = [[x for x in range(3)] for y in range(11)]
print(lista)

lista2 = [x.lower() for x in "ABcDE"]
print(lista2)

lista3 = [x*y for (x,y) in ([1,2],[3,4])]
print(lista3)

lista4 = [[x*y,(x+1)*(y+1)]*3 for x,y in ([a,a+1] for a in range(5))]
print("lista4:",lista4)