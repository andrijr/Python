class Board:
    def __init__(self,player):
        self.board = [["*","*","*"],["*","*","*"],["*","*","*"]]
        self.player = player
        self.win = False

    def checkIfWin(self):
        for x in range(0,3):
            if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and (self.board[x][2] == "X" or self.board[x][2] == "O"):
                self.win = True
                return True
        for y in range(0,3):
            if self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y] and (self.board[2][y] == "X" or self.board[2][y] == "O"):
                self.win = True
                return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and (self.board[2][2] == "X" or self.board[2][2] == "O"):
            self.win = True
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and (self.board[2][0] == "X" or self.board[2][0] == "O"):
            self.win = True
            return True
    
        return False

    def checkIfDraw(self):
        if not self.checkIfWin():
            for wiersz in self.board:
                for element in wiersz:
                    if element == "*":
                        return False
            return True
        else:
            return False

    def printTheBoard(self):
        print("  1 2 3")
        numerWiersza = 1
        for wiersz in self.board:
            print(numerWiersza, end = " ")
            for element in wiersz:
                print(element, end = " ")
            print()
            numerWiersza += 1

    def checkIfFree(self,x,y):
        return self.board[x-1][y-1] == "*"

    def changeThePlayer(self):
        if self.player == "O":
            self.player = "X"
        else:
            self.player = "O"

    def putToBoard(self,x,y):
        if self.checkIfFree(x,y):
            self.board[x-1][y-1] = self.player
            self.changeThePlayer()

    def getPlayer(self):
        return self.player

    def returnBoard(self):
        return self.board