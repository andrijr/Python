
file = open('39_plik_tekstowy.txt', 'r', encoding="UTF-8")
print(file.read())
file.close()

file = open('39_plik_tekstowy.txt', 'r', encoding="UTF-8")
print(file.readline())
file.close()


file = open('39_plik_tekstowy.txt', 'r', encoding="UTF-8")
numberOfLine = 0
for line in file:
    print(str(numberOfLine) + ':' + line )
    numberOfLine += 1
file.close()

print("----")
file = open('39_plik_tekstowy.txt', 'w', encoding="UTF-8")
file.write("to jest nowa 1 linia")
file.close()

file = open('39_plik_tekstowy.txt', 'a', encoding="UTF-8")
file.write("\nto jest nowa dopisana 2 linia")
file.close()

file = open('39_plik_tekstowy.txt', 'r', encoding="UTF-8")
print(file.read())
file.close()

print("----")
file = open('39_plik_tekstowy.txt', 'r+', encoding="UTF-8")
file.write("to jest nowa 1 linia")
print(file.read())
file.close()