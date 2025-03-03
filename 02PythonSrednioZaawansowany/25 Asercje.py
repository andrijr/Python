# Asercja jest to pewne żałożenie że w tym miejscu programu dana wartość dana zmienna jest jeżeli jest spełniony warunek
# jeżeli warunek nie jest spełniony to program powinien się wywalić
# Asercje nazywają też IRD czyli iryd
# asercja wywala program na pierwszym błędzie jaki napotka i kończy program


# a = int(input("Podaj 1 liczbę: "))
# b = int(input("Podaj 2 liczbę: "))

a = 2
b = 1
print(1/(a/b) + 1)

a = 2
b = 22
if b != 0:
    x = 1/(a/b) + 1
    suma = 0
    for i in range(int(x)):
        suma += i
    print(suma)


a = 0
b = 5
if b != 0 and a!=0 :
    assert 1/(a/b) + 1 >= 0 # jeżeli ten warunek jest prawdziwy to program się wywali i wiemy że na tej linijce
    x = 1/(a/b)  + 1
    suma = 0
    for i in range(int(x)):
        suma += i
    assert suma > 0
    print(suma)
else:
    print("liczba nie może być 0")

a = 0
b = 5
if b != 0:
    assert 1/(a/b) + 1 >= 0 # jeżeli ten warunek jest prawdziwy to program się wywali i wiemy że na tej linijce
    x = 1/(a/b) + 1
    suma = 0
    for i in range(int(x)):
        suma += i
    assert suma > 0
    print(suma)
