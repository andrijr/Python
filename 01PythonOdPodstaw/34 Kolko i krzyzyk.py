# gra kółko i krzyżyk

# 1 funkcja wyświetl plansze
def wyswietlPlansze(mapa2d):
    print("   1  2  3")
    numerWiersza = 0
    for wiersz in mapa2d:
        numerWiersza += 1
        print(numerWiersza, end="  ")
        for element in wiersz:
            print(element, end="  ")
        print("")

# 2 funkcja kto wygrywa
def wygrana(mapa2d):
    for x in range(0, 3):
        if mapa2d[x][0] == mapa2d[x][1] and mapa2d[x][1] == mapa2d[x][2] and mapa2d[x][2] == "X" or mapa2d[x][2] == "O":
            return True
    for y in range(0, 3):
        if mapa2d[0][y] == mapa2d[1][y] and mapa2d[1][y] == mapa2d[2][y] and mapa2d[2][y] == "X" or mapa2d[2][y] == "O":
            return True
    if mapa2d[0][0] == mapa2d[1][1] and mapa2d[1][1] == mapa2d[2][2] and mapa2d[2][2] == "X" or mapa2d[2][2] == "O":
        return True
    if mapa2d[0][2] == mapa2d[1][1] and mapa2d[1][1] == mapa2d[2][0] and mapa2d[2][0] == "X" or mapa2d[2][0] == "O":
        return True
    return False

# 3 funkcja remis
def remis(mapa2d):
    if not wygrana(mapa2d):
        for wiersz in mapa2d:
            for element in wiersz:
                if element == "*":
                    return False
        return True
    else:
        return False



# 4 pętla while kto zaczyna grę
graKrzyzyk = False
pobrana = 'z'
while pobrana.upper() != 'X' and pobrana.upper() != 'O':
    pobrana = input("Podaj kto zaczyna grę 'X' czy 'O': ")
    if pobrana.upper() == 'X':
        graKrzyzyk = True
    else:
        print("To nie jest poprawna liczba. Podaj  'X' lub 'O' ")



# 5 plansza startowa
plansza = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


# 6 pętla while samej gry
while (not remis(plansza)) and (not wygrana(plansza)):
    wyswietlPlansze(plansza)
    # Kto wykonuję ruch
    if graKrzyzyk:
        greKrzyzykLitera = "X"
    else:
        greKrzyzykLitera = "O"
    print("Ruch wykonuję gracz ", greKrzyzykLitera)
    # wprowadzenie współrzędnych ruchu
    try:
        x, y = [int(x) for x in input("Podaj współżędne x y: ").split()]
    except ValueError:
        print("To nie jest poprawna liczba")
        continue
    if plansza[x - 1][y - 1] == "*":
        if graKrzyzyk:
            plansza[x - 1][y - 1] = "X"
            graKrzyzyk = False
        else:
            plansza[x - 1][y - 1] = "O"
            graKrzyzyk = True
    else:
        print("Pole zajęte spróbój jeszcze raz")


# 7 wyświetlemie planszy
wyswietlPlansze(plansza)
if wygrana(plansza):
    if graKrzyzyk:
        print("Wygrała osoba grająca jako O")
    else:
        print("Wygrała osoba grająca jako X")
else:
    print("Nastąpił remis ")

# można dodać AI gra z komputerem
# if any lub if all
# może być większa plansza
