import Board

player = input("Jeżeli mają zacząć krzyżyki wpisz X, a jeżeli kółka wpisz O: ")
board = Board.Board(player)

while (not board.checkIfWin()) and (not board.checkIfDraw()):
    board.printTheBoard()
    x, y = [int(x) for x in input("Podaj współrzędne pola na którym chcesz postawić krzyżyk bądź kółko: ").split()]
    board.putToBoard(x,y)

board.printTheBoard()

if board.checkIfWin():
    if board.getPlayer() == "X":
        print("Wygrał gracz grający kółkami! Gratulujemy!")
    else:
        print("Wygrał gracz grający krzyżykami! Gratulujemy!")
else:
    print("Nastąpił remis.")