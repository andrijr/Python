# Program, który dla zadanego tekstu przedstawi alfabetyczną listę liter w nim występujących wraz z ilością wystąpień

text = input("Podaj tekst: ")
lista = []
for character in text:
    if not character in lista and character != ' ':
        lista.append(character)

sortedLista = sorted(lista)
#print(sortedLista)

listaIlosciWystapien = []
for character in sortedLista:
    ile = 0
    for litera in text:
        if litera == character:
            ile += 1
        else:
            pass
    listaIlosciWystapien.append(ile)
#print(listaIlosciWystapien)

for i in range(0,len(sortedLista)):
    print(sortedLista[i],listaIlosciWystapien[i])