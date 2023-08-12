# lcizba Armstronga to taka która raówna się sumie ich cyfr podniesionych do odpowiednich potęg
x = 371 == 3**3 + 7**3 + 1**3
print(x)

x = 12
x = (str(x)[1])
print(x)
print("----")

x = 3 % 10 # => 3
print(x)

x = 234 % 10 # => 4
print(x)
print("----")

x = 3 // 10 # => 0
print(x)

x = 234 // 10 # => 23
print(x)

print("znajdż liczby armstronga od 1 do 1000")
x1 = 0
x2 = 0
x3 = 0
for x in range(1, 1001):
    potega = len(str(x))
    if potega == 1:
        x1 = int(str(x)[0])
    if potega == 2:
        x1 = int(str(x)[0])
        x2 = int(str(x)[1])
    if potega == 3:
        x1 = int(str(x)[0])
        x2 = int(str(x)[1])
        x3 = int(str(x)[2])
    if x == x1**potega + x2**potega + x3**potega:
        print(x, "jest liczba armstronga")
print("----")


print("znajdż liczby armstronga od 1 do 1000")
for x in range(1, 1001):
    suma = 0
    kopia = x
    potega = len(str(x))
    # print("liczba", x, "potęga", potega)
    while kopia > 0:
        cyfra = kopia % 10
        suma += cyfra ** potega
        kopia //= 10
        # print("cyfra", cyfra, "suma", suma, "kopia", kopia)
    if suma == x:
        print(x, "liczba armstronga")





print("znajdź liczby armstronga podaj zakres")
od = int(input("podaj liczbę od: "))
do = int(input("podaj liczbę do: "))
for x in range(od, do+1):
    dlugosc = len(str(x))
    suma = 0
    liczba = x
    while x !=0:
        reszta = x % 10
        suma += reszta ** dlugosc
        x = x // 10
    if suma == liczba:
         print(liczba, " jest liczbą armstronga")

