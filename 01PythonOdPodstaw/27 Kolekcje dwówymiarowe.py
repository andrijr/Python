# jednowymiarowa lista (kolekcja)
lista = [1, 2, 3, 4, 5]
print(lista)

# dwówymiarowa lista (kolekcja)
lista = [[1,2,3], [4,5]]
print(lista)
print(lista[1])
print(lista[0][0])
print(lista[1][0])
print("----")

for i in lista:
    print(i)

for i in lista:
    print(i, end=" ")
print("\n")

for i in lista:
    for j in i:
        print(j, end=" ")
print("\n")

for x in range(0, len(lista)):
    for y in range(0, len(lista[x])):
        print(lista[x][y], end=" ")
print()

szachownica = ( ("w", "s", "g", "h", "k", "g" , "s", "w"), ("p", "p", "p", "p", "p", "p" , "p", "p"), ("*", "*", "*", "*", "*", "*" , "*", "*"),
        ("*", "*", "*", "*", "*", "*" , "*", "*"), ("*", "*", "*", "*", "*", "*" , "*", "*"), ("*", "*", "*", "*", "*", "*" , "*", "*"),
        ("p", "p", "p", "p", "p", "p" , "p", "p"), ("w", "s", "g", "h", "k", "g" , "s", "w") )
print(szachownica)
print()

for i in szachownica:
    for j in i:
        print(j, end="  ")
    print()