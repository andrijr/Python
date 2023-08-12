import math

print("znajdź wszystkie liczby piwersze z przedziału od 1 do 1000")
for liczba in range(2, 1000):
    liczbaPierwsza = True
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            liczbaPierwsza = False
            print("liczba ", liczba, "dzieli się przez ", dzielnik)
    if liczbaPierwsza:
        print("liczba pierwsza ", liczba)
print("----")



print("znajdź wszystkie liczby piwersze z przedziału od 1 do 1000")
for liczba in range(2, 1000):
    liczbaPierwsza = True
    for dzielnik in range(2, int(math.sqrt(liczba))):
        if liczba % dzielnik == 0:
            liczbaPierwsza = False
            #print("liczba ", liczba, "dzieli się przez ", dzielnik)
    if liczbaPierwsza:
        print("liczba pierwsza ", liczba)

