# Program, który dla zadanego tekstu przedstawi alfabetyczną listę liter w nim występujących wraz z ilością wystąpień

text = input("Podaj tekst: ")
setOfLetters = set(text).difference(' ')
dictOfLetters = dict((letter,text.count(letter)) for letter in setOfLetters)
listOfLetters = sorted(dictOfLetters.keys())
for letter in listOfLetters:
    print(letter, dictOfLetters[letter])