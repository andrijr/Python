class Numbers:
    numbersSum = 0

    def __init__(self, numbers = []):
        self.l = numbers
        self.numbers = self.l

    def sumNumbers(self):
        summary = 0
        for x in self.numbers:
            summary += x
        return summary

    def productNumbers(self):
        product = 1
        for x in self.numbers:
            product *= x
        return product

    def addNumberToList(self,number):
        self.numbers.append(number)
        Numbers.prepareNumbersSum(number)

    @classmethod
    def prepareNumbersSum(cls, number):
        cls.numbersSum += number

    @staticmethod
    def subtractNumbers(a,b):
        print("Jestem statyczną metodą")
        return a - b

    @classmethod
    def printInformationAboutMe(cls):
        print("Jestem klasową metodą")
        print("wywołaną na rzecz klasy", cls.__name__)