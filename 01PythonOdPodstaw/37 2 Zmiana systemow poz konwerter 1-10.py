# funkca z podaniem na jaki system konwertować
# skrócić ta funkcję
# pozbyć się funkcję naDziesiątne ws zystko zrobić na jednej
# urzytkownik podaję z jakiego systemu na jaki ma przekonwertować



import string


#  2  >> 10 ; 1100 =>  0*2**0 + 0*2**1 + 1*2**2 + 1*2**3 => 12
def Od1Do10naDziesiatkowy(n:int, zJakiego:int):
    if 1 <= zJakiego <= 10:
        # od 1 do 10 na 10-kowy
        wynik = 0
        potega = 0
        while n > 0:
            reszta = n % 10
            wynik += reszta * zJakiego ** potega
            #print('n = ', n , 'zJakiego = ', zJakiego, 'reszta = ', reszta, 'potega = ', potega,  'wynik = ', wynik)
            n //= 10
            potega += 1
        return wynik
    else:
        print("wprowadź poprawny system konwersji od 1 do 10. Konwersja na 10-kowy system")


#  10 >> 2  ; 12 => 12 % 2 = 0 | 12 // 2 => 6 % 2 = 0 | 6 // 2 => 3 % 2  = 1 | 3 // 2 => 1 % 2 = 1 => 0011 => 1100
def zDziesiatkowegoNaOd1Do10(n:int,  naJaki:int):
    if 1 <= naJaki <= 10:
        # z 10-kowego na od 1 do 10
        wynik = 0
        potega = 0
        listaOutput = []
        tekstOutput = ''
        while n > 0:
            reszta = n % naJaki
            #print('n = ', n , 'naJaki = ', naJaki, 'reszta = ', reszta, 'potega = ', potega,  'wynik = ', wynik)
            listaOutput.append(reszta)
            n = n // naJaki
            potega += 1
        listaOutput.reverse()
        for i in listaOutput:
            tekstOutput += str(i)
        wynik = int(tekstOutput)
        return wynik
    else:
        print("wprowadź poprawny zakres korwersji od 1 do 10")


#  2  >> 10 ; 1100 =>  0*2**0 + 0*2**1 + 1*2**2 + 1*2**3 => 12
#  10 >> 2  ; 12 => 12 % 2 = 0 | 12 // 2 => 6 % 2 = 0 | 6 // 2 => 3 % 2  = 1 | 3 // 2 => 1 % 2 = 1 => 0011 => 1100
def zmianaSystemuPozycyjnegoOd1Do10(n:int, zJakiego:int, naJaki:int):
    if 1 <= zJakiego <= 10 and 1 <= naJaki <= 10:
        # od 1 do 10 na 10-kowy
        wynik1 = 0
        potega1 = 0
        while n > 0:
            reszta1 = n % 10
            wynik1 += reszta1 * zJakiego ** potega1
            #print('n = ', n , 'zJakiego = ', zJakiego, 'reszta = ', reszta1, 'potega = ', potega1,  'wynik = ', wynik1)
            n //= 10
            potega1 += 1

        # z 10-kowego na od 1 do 10
        wynik2 = 0
        potega2 = 0
        listaOutput = []
        tekstOutput = ''
        while wynik1 > 0:
            reszta2 = wynik1 % naJaki
            #print('n = ', wynik1 , 'naJaki = ', naJaki, 'reszta = ', reszta2, 'potega = ', potega2,  'wynik = ', wynik2)
            listaOutput.append(reszta2)
            wynik1 = wynik1 // naJaki
            potega2 += 1
        listaOutput.reverse()
        for i in listaOutput:
            tekstOutput += str(i)
        wynik2 = int(tekstOutput)
        return wynik2
    else:
        print("wprowadź poprawny zakres korwersji od 1 do 10")










print(Od1Do10naDziesiatkowy(1100, 2))
print(zDziesiatkowegoNaOd1Do10(12, 2))
print(zmianaSystemuPozycyjnegoOd1Do10(1100, 2, 2))





