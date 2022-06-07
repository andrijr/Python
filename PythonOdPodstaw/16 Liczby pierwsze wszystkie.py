import math
# wyswietl wszystkie liczby od 1 od 1000

for liczba in range(2,1000):
    liczbaPierwsza = True
    #for dzielnik in range(2, math.sqrt(liczba)):
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            liczbaPierwsza = False
            #print("liczba ", liczba, "dzieli się przez", dzielnik)
    if liczbaPierwsza:
        print("Liczba", liczba, "jest liczbą pierwszą")
    else:
        continue
        # print("")
        # print("Liczba", liczba, "nie jest liczbą pierwszą")
