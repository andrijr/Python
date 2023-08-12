# każda kolekcja jest obiektem

def dodaj(a, b):
    return a+b

def odejmij(a, b):
    return a-b

def pomnoz(a, b):
    return a*b

def podziel(a, b):
    return a/b

def podzielCalkowicie(a, b):
    return a//b

def resztaModulo(a, b):
    return a%b



tupla = (1,2)
lista = [1, 2, 3, 'a', 'b', '4', tupla]
print(lista)
lista = [1, 2, 3, 'a', 'b', '4', tupla, dodaj(4,5)]
print(lista)
lista = [1, 2, 3, 'a', 'b', '4', tupla, dodaj]
print(lista)


print("1-----")
lista = [dodaj(3,2),odejmij(3,2), pomnoz(3,2), podziel(3,2), podzielCalkowicie(3,2), resztaModulo(3,2)]
listaOpis= ['dodaj','odejmij', 'pomnoz', 'podziel', 'podzielCalkowicie', 'resztaModulo']
print(lista)

listaFunkcji = [dodaj,odejmij, pomnoz, podziel, podzielCalkowicie, resztaModulo]
listaOpis= ['dodaj','odejmij', 'pomnoz', 'podziel', 'podzielCalkowicie', 'resztaModulo']
print(listaFunkcji)

print("2-----")
x = 5
y = 2
for i in range(1,len(listaFunkcji)):
    print(listaOpis[i],x, y, '= ', listaFunkcji[i](x,y))

print("3-----")

for funkcja in listaFunkcji:
    print(funkcja(x,y))