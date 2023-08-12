
tekst = "to jest nasz tekst"
lista = []
for znak in tekst:
    if not znak in lista and znak != ' ':
        lista.append(znak)
print(lista)

posortowanaLista = sorted(lista)
print(posortowanaLista)

listaIlosciWystapien = []
for znak in posortowanaLista:
    ile = 0
    for litera in tekst:
        if litera == znak:
            ile += 1
        else:
            pass
    listaIlosciWystapien.append(ile)
print(listaIlosciWystapien)

for i in range(0, len(posortowanaLista)):
    print(posortowanaLista[i], listaIlosciWystapien[i])