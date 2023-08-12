
# 1 sprawdzić jak otrzymać liste kluczy bądź listę wartości ze słownika
# 2 możesz sprawdzić jakie są inne kolekcję
# 3 stworzenie podobnego słownika może być uporządkowany którego wartościami zawsze listy liczb
# 4 następnie otrzymać listę wartośći lista z list
# 5 wyświetlić wszystkie elementy z tych wewnętrznych list oraz sumę wszystkich liczbowych wartości
# 6 podobnie słownik zamień na tuple

print('---1')
slownik = {"Agni": 333, "Andrij": 444, "Anastazja" : 111, "Adam": 222}
print(slownik)
for i in slownik:
    print(i, slownik[i], end=" ")

print('\n---2')
string = "tekst"
lista = [1, 2, 3]
tupla = (1, 2, 3)
slownik2 = {'a':1, 'b':2, 'c':3}
zbior = {1, 2, 3}


lista = []
suma = 0
for i in slownik:
    print(slownik[i], end=" ")
    lista.append(slownik[i])
    suma += slownik[i]
print()
print(lista)
print(suma)




