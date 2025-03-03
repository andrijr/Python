class Numbers:
    numbersSum = 0 # pole klasy Numbers
    def __init__(self, numbers = []):
        self.numbers = numbers
    def sumNumbers(self):
        summary = 0
        for x in self.numbers:
            summary += x
        return  summary
    def prouctNumbers(self):
        product = 1
        for x in self.numbers:
            product *= x
        return product
    def addNumbersToList(self, number):
        self.numbers.append(number)
        Numbers.prepareNumbersSum(number)
    @classmethod
    def prepareNumbersSum(cls, number):
        cls.numbersSum += number


# dekoratory zaczynamy @ mawpą
# metoda oznaczona takim dekoratorem nie potrzebuję instancji nie potrzebuję obiektu
    @staticmethod
    def substractNumbers(a,b):
        print("Jestem statyczną metodą")
        return a - b

    # classmethod nie potrzebuję objektu tak jak staticmethod
    @classmethod
    def printInformationAboutMe(cls): # cls oznacza tutaj klase metody klasowe mają dostęp do klasy
        print("Jestem klasową metodą")
        print("Wywolano na rzecz kalsy", cls, cls.__name__)


