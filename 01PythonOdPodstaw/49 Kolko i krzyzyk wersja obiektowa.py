import Board_49_1

#while board.player

player = input("Podaj kto zaczyna grę 'X' czy 'O': ").upper()
while player !='X' and  player != 'O':
    print("to nie jest poprawny znak podaj 'X' lub 'O' ")
    player = input("Podaj kto zaczyna grę 'X' czy 'O': ").upper()

board = Board_49_1.Board(player)

while (not board.checkIfWin() and (not board.checkIfDraw())):
    board.printTheBoard()
    # Kto wykonuję ruch
    print("Ruch wykonuję gracz ", board.getPlayer())
    # wprowadzenie współrzędnych ruchu
    try:
        x, y = [int(x) for x in input("Podaj współżędne x y: ").split()]
    except ValueError:
        print("To nie jest poprawna liczba")
        continue
# do poprawy z lekcji 34

    # if plansza[x - 1][y - 1] == "*":
    #     if graKrzyzyk:
    #         plansza[x - 1][y - 1] = "X"
    #         graKrzyzyk = False
    #     else:
    #         plansza[x - 1][y - 1] = "O"
    #         graKrzyzyk = True
    # else:
    #     print("Pole zajęte spróbój jeszcze raz")

    board.putToBoard(x,y)

board.printTheBoard()

if board.checkIfWin():
    if board.getPlayer() == 'X':
        print("Wygrała osoba grająca jako O")
    else:
        print("Wygrała osoba grająca jako X")
else:
    print("Nastąpił remis ")