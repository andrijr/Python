# kiedy urzywamy wyrażenie lambda
# kiedy chcemy to wyrażenie urzyć kikukrotnie niema potrzeby urzywania funkcji
# lambda to bardzo proste wyrażenie funkcyjne nie może tu być żadnego słowa kluczowego
# wyrażen lambda urzywa się nie dla tego żeby skrócić zapis
# wyrażeń lambda urzywa się do domknięcia
# wyrażenie lambda urzywamy rozsądnie ponieważ zazwyczaj utrudniająją czytanie kodu
# wyrażenia listowe lepej się debaguję niż wyrażenia lambda


def dodaj(a,b):
    return a+b

print(dodaj(10,20))

dodaj2 = lambda c,d: c+d
print(dodaj2(10,20))

lista = [dodaj(x,y) for x,y in ([10, 10],[11, 13])]
print(lista)

lista = [dodaj2(x,y) for x,y in ([10, 10],[11, 13])]
print(lista)

wynik = (lambda a, b: a**3+3*a-b**2 ) (10,20)
print(wynik)

print("---")
#domknięcia: x+n

def make_incrementor(n):
    return lambda x: x+n

dodaj100 = make_incrementor(100)
print(dodaj100(11))

lista = sorted(range(3,12))
print(lista)

lista = sorted(range(-3,12))
print(lista)

lista = sorted(range(-3,12), key= lambda x: x**2)
print(lista)