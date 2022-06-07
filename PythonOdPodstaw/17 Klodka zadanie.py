import math
# kłodka jest 5 cyfrowa
# kiczba kłodki była liczbą pierwszą
# suma liczb była z zakresu 30 i 40
# nie było 0
# czy istnieje taka kłódka i ile jest porawnych możliwości
ilosc = 0
licznik = 0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if 30 <= a + b + c + d + e <= 40:
                        licznik = int(str(a) + str(b) + str(c) + str(d) + str(e))
                        liczbaPierwsza = True
                        #print("licznik",a, b, c, d, e)
                        for mianownik in range(2, int(math.sqrt(10000))):
                            if licznik % mianownik == 0:
                                LiczbaPierwsza = False
                                #print(a, b, c, d, e)
                        if liczbaPierwsza == True:
                            print(a, b, c, d, e)
                            ilosc += 1
print("liczba wariantów kłódki: ", ilosc)
