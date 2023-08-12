lista = [[1,2,3], [4,5]]


print(lista[0][1])
print(lista[1][0])

for i in lista:
    for j in i:
        print(j,end=' ')

print()

for x in range(0,len(lista)):
    for y in range(0,len(lista[x])):
        print(lista[x][y], end=" ")

szachownica = (("W","S","G","H","K","G","S","W"),("P","P","P","P","P","P","P","P"),("*","*","*","*","*","*","*","*"),
         ("*", "*", "*", "*", "*", "*", "*", "*"),("*","*","*","*","*","*","*","*"),("*","*","*","*","*","*","*","*"),
         ("P", "P", "P", "P", "P", "P", "P", "P"), ("W","S","G","H","K","G","S","W"))

print()
print()

for i in szachownica:
    for j in i:
        print(j,end=' ')
    print()