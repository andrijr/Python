class Temp:
    def __init__(self):
        self.a = 3
        self.__a = 5

    def printMe(self):
        print(self.a)
        print(self.__a)