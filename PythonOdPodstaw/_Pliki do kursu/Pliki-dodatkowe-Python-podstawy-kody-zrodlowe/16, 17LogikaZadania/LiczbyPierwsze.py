import math

# Liczba pierwsza - taka liczba naturalna >= 2, która dzieli się tylko przez 1 i samą siebie

# liczba = int(input("Podaj liczbę: "))
#
# liczbaPierwsza = True
#
# for dzielnik in range(2,liczba):
#     if liczba % dzielnik == 0:
#         liczbaPierwsza = False
#         print("Podana liczba", liczba, "dzieli się przez", dzielnik)
#
# if liczbaPierwsza:
#     print("Liczba jest liczbą pierwszą")


for liczba in range(2,1000001):
    liczbaPierwsza = True
    for dzielnik in range(2,int(math.sqrt(liczba))):
        if liczba % dzielnik == 0:
            liczbaPierwsza = False
            # print("Podana liczba", liczba, "dzieli się przez", dzielnik)
    if liczbaPierwsza:
        print("Liczba", liczba, "jest liczbą pierwszą")
    else:
        print("Liczba", liczba, "nie jest liczbą pierwszą")

