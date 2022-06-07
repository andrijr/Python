# Napisz program liczący średnią harmoniczną
# Napisz program liczący średnią geometryczną
# Napisz program liczący średnią kwadratową

import math

# Napisz program liczący średnią harmoniczną
# n = int(input("Z ilu liczb chcesz wyliczyć średnią harmoniczną? Podaj liczbę: "))
# a = 0.0
# suma = 0.0
#
# for x in range(0, n):
#     a = float(input("podaj lczbę: "))
#     suma += 1/a
# suma = n/suma
# print("wynik: ", suma)


# Napisz program liczący średnią geometryczną
# n = int(input("Z ilu liczb chcesz wyliczyć średnią geometryczną? Podaj liczbę: "))
# a = 0.0
# iloczyn = 1
#
# for x in range(0, n):
#     a = float(input("podaj lczbę: "))
#     iloczyn *=  a
# iloczyn = iloczyn ** (1 / n)
# print("wynik: ", iloczyn)


# Napisz program liczący średnią kwadratową
n = int(input("Z ilu liczb chcesz wyliczyć średnią kwadratową? Podaj liczbę: "))
a = 0.0
suma = 0.0

for x in range(0, n):
    a = float(input("podaj lczbę: "))
    suma +=  a ** 2
suma = (suma / n) ** (1/2)
print("wynik: ", suma)