# 5 w systemie 10 to 101 w systemie dwójkowym
# 101 => 5; 101 czytając od tyłu to kolejne potęgi 2  co daję  1 2 4 czyli mamy jedną 1 zero 2 i jedną 4 co daję na 5
# 5 => 101 ; wystarczy liczbę dzielić na 2 i spisywac resztę. 5 podzielić na 2 to 2 i reszta 1; wynik 2 dzielimy zmowu na 2
# to wynik 1 i reszta 0 ; wynik 1 dzielimy na 2 to się równa 0 i reszta 1 i otrzymujemy 101



def naDziesietny(n):
    potega = 1
    wynik = 0
    while n > 0:
        wynik += (n % 10) * potega
        potega *= 2
        n //= 10
    return wynik



def naDwojkowy(n):
    lista = []
    while n > 0:
        lista.append(n%2)
        n //= 2
    lista.reverse()
    return lista


def naDwojkowy_2(n):
    lista = []
    while n > 0:
        lista.append(n%2)
        n //= 2
    lista.reverse()
    wynik = 0
    for element in lista:
        wynik += element
        wynik *= 10
    wynik //=10
    return wynik


print(naDziesietny(1011))
print(naDwojkowy(11))
print(naDwojkowy_2(11))


