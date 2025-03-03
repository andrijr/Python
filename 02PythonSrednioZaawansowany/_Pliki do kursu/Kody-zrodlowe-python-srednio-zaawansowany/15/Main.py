#def dodaj(a,b):
#    return a+b

dodaj = lambda a,b: a+b
print(dodaj(10,20))

lista = [dodaj(x,y) for x,y in ([10,10],[11,13])]
print(lista)

print((lambda a,b:a**3+3*a-b**2)(10,20))

#Domknięcia
def make_incrementor(n):

    return lambda x: x+n

f = make_incrementor(100)
print(f(11))

lista = sorted(range(-3,12),key = lambda x: x**2)
print(lista)

