# file = open("plik_przykladowy.txt",'r',encoding="utf8")
#
# numberOfLine = 0
# textToWrite = ""
# for line in file:
#     textToWrite += str(numberOfLine) + ": " + line
#     numberOfLine += 1
#
# file.close()
#
# file = open("plik_przykladowy.txt",'w',encoding="utf8")
#
# file.write(textToWrite)
#
# file.close()


file = open("plik_przykladowy.txt",'r+',encoding="utf8")

numberOfLine = 0
for line in file:
    print(str(numberOfLine) + ": " + line, end = "")
    numberOfLine += 1

file.write("\nKoniec")

file.close()