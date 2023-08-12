# liczba jest pierwsza taka liczba naturalna która dzieli się przez 1 i przez samą siebie

print("znajdź czy wprowadzona wartość to liczba pierwsza")
liczba = int(input('Podaj liczbę: '))
liczbaPierwsza = True
for dzielnik in range(2, liczba):
    if liczba % dzielnik == 0:
        print("liczba ", liczba, " dzili sie przez ", dzielnik)
        liczbaPierwsza = False
if liczbaPierwsza:
    print("liczba", liczba, "jest liczbą pierwszą")


