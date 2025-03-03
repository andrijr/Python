# 5 w systemie 10 to 101 w systemie dwójkowym
# 101 => 5; 101 czytając od tyłu to kolejne potęgi 1 2 4 8 16 itd czyli 1*2**0  0*2**1 1*2**2 itd 2**3 2**4
# co w tym przykładzie daję kolejne potęgi 1 2 4 bo liczba 101 to trzy znaki
# czyli mamy jedną 1 do potęgi 1 daje 1 + 0 do potęgi 2 daje 0 + 1 do potęgi 4 co daję 4
# razem = 1 + 0 + 4 = 5

# 5 => 101 ; wystarczy liczbę 5 dzielić na 2 i spisywac resztę.
# 5 podzielić na 2 to 2 i reszta 1; wynik 2
# dzielimy zmowu na 2 to wynik 1 i reszta 0
#  wynik 1 dzielimy na 2 to się równa 0 i reszta 1 i otrzymujemy 101



def naDziesietny(n):
    potega = 1
    wynik = 0
    while n > 0:
        wynik += (n % 10) * potega
        potega *= 2
        n //= 10
        # print("wynik", wynik)
        # print("---")
        # print("n", n)
        # print("potęga", potega)

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
print("---")
print(naDwojkowy(11))
print(naDwojkowy_2(11))


