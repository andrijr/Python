silnia = 1*2*3*4*5
print(silnia)

# jest to zwykła funkcja nie jest to funkcja rekurencyjna
def silnia(n:int):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik

# jest to funkcja rekurencyjna. funkcja rekurencyjna wywołuję sama siebie.
def silniaRekurencyjna(n:int):
    if n == 1:
        return 1
    else:
        return n * silniaRekurencyjna(n -1)


print(silnia(5))
print(silniaRekurencyjna(5))


# jest to funkcja rekurencyjna. funkcja rekurencyjna wywołuję sama siebie.
def silniaRekurencyjna2(n:int):
    print("funjcja została wywołana dla n = ", n)
    if n == 1:
        return 1
    else:
        temp = n * silniaRekurencyjna(n -1)
        print(temp)
        return n * silniaRekurencyjna(n -1)

print("---")
print(silniaRekurencyjna2(5))
