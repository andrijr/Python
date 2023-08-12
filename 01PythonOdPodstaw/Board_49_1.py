class Board:
    def __init__(self, player): # metoda specjalna init która przechowuję informacje
        self.board = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']] # plansza
        self.player = player.upper() # gracz X czy Y
        self.win = False # wygrana

    def checkIfWin(self): # czy wygrana
        for x in range(0, 3):
            if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and self.board[x][2] == "X" or self.board[x][2] == "O":
                self.win = True
                return True
        for y in range(0, 3):
            if self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y] and self.board[2][y] == "X" or self.board[2][y] == "O":
                self.win = True
                return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] == "X" or self.board[2][2] == "O":
            self.win = True
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] == "X" or self.board[2][0] == "O":
            self.win = True
            return True
        self.win = False
        return False

    def checkIfDraw(self): # remis
        if not self.checkIfWin():
            for wiersz in self.board:
                for element in wiersz:
                    if element == "*":
                        return False
            return True
        else:
            return False

    def printTheBoard(self): # wyświetl plansze
        print("   1  2  3")
        numerWiersza = 0
        for wiersz in self.board:
            numerWiersza += 1
            print(numerWiersza, end="  ")
            for element in wiersz:
                print(element, end="  ")
            print("")

    def checkIfFree(self, x, y):
        return  self.board[x-1][y-1] == '*'

# do poprawy z likcji 34

    # def checkIfFree(self, x, y):
    #     # return  self.board[x-1][y-1] == '*'
    #
    #     if self.board[x - 1][y - 1] == "*":
    #         if self.player() == 'X':
    #             self.board[x - 1][y - 1] = "X"
    #             self.player() = 'O'
    #         else:
    #             self.board[x - 1][y - 1] = "O"
    #             self.player() = 'X'
    #     else:
    #         print("Pole zajęte spróbój jeszcze raz")


    def changeThePlayer(self): # zmień gracza
        if self.player == 'O':
            self.player = 'X'
        else:
            self.player = 'O'

    def putToBoard(self, x, y):
        if self.checkIfFree(x,y):
            self.board[x-1][y-1] = self.player
            self.changeThePlayer()

    def getPlayer(self):
        return self.player

    def returnBoard(self):
        return self.board