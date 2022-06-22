# a + b + c = a ** n + b ** n + c ** n

a = 10000

for liczba in range(0, a):
    kopia = liczba
    suma = 0
    # n = int(len(str(liczba)))
    while kopia > 0:
        cyfra = kopia % 10
        suma += cyfra ** len(str(liczba))
        kopia //= 10

    if suma == liczba:
        print(liczba, "liczba Armstronga")
