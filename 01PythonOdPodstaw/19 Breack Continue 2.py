
liczba = int(input("podaj liczbę: "))
liczbaPierwsza = True
for dzielnik in range(2, liczba):
    if liczba % dzielnik == 0:
        print(liczba, "jest to liczba złożona")
        liczbaPierwsza = False
        break
if liczbaPierwsza:
    print(liczba, "jest liczbą pierwszą")
