# funkca z podaniem na jaki system konwertować
# skrócić ta funkcję
# pozbyć się funkcję naDziesiątne ws zystko zrobić na jednej
# urzytkownik podaję z jakiego systemu na jaki ma przekonwertować



import string



#  16  >> 10 ; FA => A(10)*16**0 + F(15)*16**1  => 10 + 240 => 250
#  10 >> 18  ; 250 => 250 % 18 = 16(G) | 250 // 18 => 13 % 18 = 13(D)) >> GD >> DG
def zmianaSystemuPozycyjnegoOd1Do36(n:str, zJakiego:int, naJaki:int):
    listaPositionSystem = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ] + list(string.ascii_uppercase)
    #print(listaPositionSystem)

    if 1 <= zJakiego <= 36 and 1 <= naJaki <= 36:
        # od 1 do 36 na 10-kowy
        wynik1 = 0
        potega1 = 0
        n = str(n)
        listaInput = []
        listaInput[:0] = n
        listaInput.reverse()
       #while n > 0:
        for i in listaInput:
            reszta1 = listaPositionSystem.index(i)
            wynik1 += reszta1 * zJakiego ** potega1
            #print('n1 = ', n , 'zJakiego = ', zJakiego, 'reszta = ', reszta1,  'potega = ', potega1,  'wynik = ', wynik1)
            potega1 += 1
        #return wynik1

        # z 10-kowego na od 1 do 10
        wynik2 = 0
        potega2 = 0
        listaOutput = []
        tekstOutput = ''
        while wynik1 > 0:
            reszta2 = wynik1 % naJaki
            #print('n2 = ', wynik1 , 'naJaki = ', naJaki, 'reszta = ', reszta2, listaPositionSystem[reszta2], 'potega = ', potega2,  'wynik = ', wynik2)
            wynik1 = wynik1 // naJaki
            listaOutput.append(listaPositionSystem[reszta2])
            potega2 += 1
        listaOutput.reverse()
        for i in listaOutput:
            tekstOutput += str(i)
        #wynik2 = int(tekst)
        return tekstOutput
    else:
        print("wprowadź poprawny zakres korwersji od 1 do 36")









print(zmianaSystemuPozycyjnegoOd1Do36('FA', 16, 18))
print(zmianaSystemuPozycyjnegoOd1Do36('C', 14, 16))
print(zmianaSystemuPozycyjnegoOd1Do36('1111', 1, 16))




