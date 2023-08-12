# 5 = 101   5:2 = 2 r 1  2:2 = 1 r 0   1:2 = 0 r 1
# 101011101 = 1*256 + 0*128 + 1*64 + 0*32 + 1*16 + 1*8 + 1*4 + 0*2 + 1 = 349

def naDwojkowy(n):
    lista = []
    while n > 0:
        lista.append(n%2)
        n //= 2
    lista.reverse()
    wynik = 0
    for element in lista:
        wynik += element
        wynik *= 10
    wynik //= 10
    return wynik

def naDziesietny(n):
    potega = 1
    wynik = 0
    while n > 0:
        wynik += (n % 10) * potega
        potega *= 2
        n //= 10
    return wynik

n = int(input("Podaj liczbę w systemie dwójkowym: "))
print("Liczba ta w systemie dziesiętnym wynosi: ", naDziesietny(n))

m = int(input("Podaj liczbę w systemie dziesiętnym: "))
print("Liczba ta w systemie dwójkowym wynosi: ", naDwojkowy(m))