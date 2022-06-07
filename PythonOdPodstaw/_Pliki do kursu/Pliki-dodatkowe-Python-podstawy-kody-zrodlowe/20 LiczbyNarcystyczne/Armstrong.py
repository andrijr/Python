# for x in range (1,10):
#     for y in range (0,10):
#         for z in range (0,10):
#             if x * 100 + y * 10 + z == x**3 + y**3 + z**3:
#                 print(x * 100 + y * 10 + z)

for liczba in range (0,100000000):
    suma = 0
    kopia = liczba
    while kopia > 0:
        cyfra = kopia % 10
        suma += cyfra ** len(str(liczba))
        kopia //= 10

    if suma == liczba:
        print(liczba, "jest liczbą Armstronga")

