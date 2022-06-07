#silnia(10) = 1*2*3*4*5*6*7*8*9*10

def silnia(n: int):
    wynik = 1
    for i in range (2, n+1):
        wynik *= i
    return wynik

def silniaRekurencyjna(n: int):
    print("Funkcja została wywołana dla n =", n)
    if n == 1:
        return 1
    else:
        temp = n * silniaRekurencyjna(n-1)
        print("Pośredni wynik dla", n, "* silnia(", n-1, "):",temp)
        return temp

x = int(input("Podaj liczbę dla której chcesz obliczyć silnię: "))
#print("Silnia z liczby", x, "wynosi:",silnia(x))
print("Silnia z liczby", x, "wynosi:",silniaRekurencyjna(x))
