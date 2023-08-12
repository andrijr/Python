def wyswietlPlansze(mapa2D):
    print("  1 2 3")
    numerWiersza = 1
    for wiersz in mapa2D:
        print(numerWiersza, end = " ")
        for element in wiersz:
            print(element, end = " ")
        print()
        numerWiersza += 1

def wygrana(mapa2D):
    for x in range(0,3):
        if mapa2D[x][0] == mapa2D[x][1] and mapa2D[x][1] == mapa2D[x][2] and (mapa2D[x][2] == "X" or mapa2D[x][2] == "O"):
            return True
    for y in range(0,3):
        if mapa2D[0][y] == mapa2D[1][y] and mapa2D[1][y] == mapa2D[2][y] and (mapa2D[2][y] == "X" or mapa2D[2][y] == "O"):
            return True
    if mapa2D[0][0] == mapa2D[1][1] and mapa2D[1][1] == mapa2D[2][2] and (mapa2D[2][2] == "X" or mapa2D[2][2] == "O"):
        return True
    if mapa2D[0][2] == mapa2D[1][1] and mapa2D[1][1] == mapa2D[2][0] and (mapa2D[2][0] == "X" or mapa2D[2][0] == "O"):
        return True

    return False

def remis(mapa2D):
    if not wygrana(mapa2D):
        for wiersz in mapa2D:
            for element in wiersz:
                if element == "*":
                    return False
        return True
    else:
        return False

graKrzyzyk = False
pobrana = input("Jeżeli mają zacząć krzyżyki wpisz X, a jeżeli kółka wpisz O: ")
if pobrana == "X":
    graKrzyzyk = True
plansza = [["*","*","*"],["*","*","*"],["*","*","*"]]

while (not remis(plansza)) and (not wygrana(plansza)):
    wyswietlPlansze(plansza)
    x, y = [int(x) for x in input("Podaj współrzędne pola na którym chcesz postawić krzyżyk bądź kółko: ").split()]
    if plansza[x-1][y-1] == "*":
        if graKrzyzyk:
            plansza[x-1][y-1] = "X"
            graKrzyzyk = False
        else:
            plansza[x-1][y-1] = "O"
            graKrzyzyk = True

wyswietlPlansze(plansza)

if wygrana(plansza):
    if graKrzyzyk:
        print("Wygrał gracz grający kółkami! Gratulujemy!")
    else:
        print("Wygrał gracz grający krzyżykami! Gratulujemy!")
else:
    print("Nastąpił remis.")

# Napisać AI - przeciwnik komputer. Komputer niech losuje dwie liczby obie z przedziału 0 2
# if any, if all
# Stworzyć podobną grę dla planszy o wymiarze 5x5. Załóżenie: cztery takie same znaki do wygranej