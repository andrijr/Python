# kłódka jest 5 cyfrowa
# liczba kłódki była liczbą pierwszą
# suma cyfr z zakresu 30 i 40
# nie było żadnego 0 ok

liczbaPierwsza = True
sumaKlodki = 0
liczba = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    if 30 < a+b+c+d+e < 40:
                        sumaKlodki  = a + b + c + d + e
                        # print(a, b, c, d, e, "suma ", sumaKlodki)
                        # liczba += 1
                        liczbaPierwsza = True
                        for dzielnik in range(2, sumaKlodki):
                            if sumaKlodki % dzielnik == 0:
                                liczbaPierwsza = False
                                # print("liczba ", sumaKlodki, "podzielna przez ", dzielnik)
                        if liczbaPierwsza:
                            liczba += 1
                            print(a, b, c, d, e, "suma", sumaKlodki)
print("liczba rozwiązań ", liczba)

