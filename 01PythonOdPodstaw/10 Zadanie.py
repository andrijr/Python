import math

# Napisz programy
# liczące średnią harmoniczną
# średnią geometryczną
# średnią kwadratową


# średnia aretmetyczna = (a1 + a2 + a3) / n
# średnia geometryczna = (a1 * a2 * a3) ** (1/n)
# średnia harmoniczna = n / ( 1/a1 + 1/a2 + 1/a3)
# średnia kwadratowa = ( (a1**2 + a2**2 + a3**2) / n ) ** 2

# Kolejność działań w python
# Nawiasy posiadają najwyższy priorytet
# unkcja potęgowania posiada kolejny najwyższy priorytet
# Mnożenie i oba typy dzieleń mają ten sam priorytet, który jest wyższy niż dodawanie i odejmowanie
# Operatory o tym samym priorytecie obliczane są od lewej do prawej


print("Podaj kolejne liczby do wyliczenia średnich, podaj 0 aby obliczyć: ")
suma = 0
geometryczna = 1
harmoniczna = 0
kwadratowa = 0
licznik = 0
for x in range(0,1000):
    a = float(input("Podaj liczbę: "))
    if a != 0:
        licznik +=1
        suma += a
        geometryczna *= a
        harmoniczna += (1 / a)
        kwadratowa += a**2
    else:
        break
suma = suma / licznik
geometryczna = geometryczna ** (1 / licznik)
harmoniczna = licznik / harmoniczna
kwadratowa = (kwadratowa / licznik) ** 0.5
print("średnia aretmetyczna: ", suma)
print("średnia geometryczna: ", geometryczna)
print("średnia harmoniczna: ", harmoniczna)
print("średnia kwadratowa: ", kwadratowa)
