phonebook = {"Karol Kurek": [111111111,"Słoneczna", 26], "Andrew Max": [222222222,"Słoneczna", 26], "Jan Kowalski":[123456789,"Słoneczna", 26], "Ktoś Inny":[1,2]}
# Klucz-Wartość, Key-Value Coding
print(phonebook["Ktoś Inny"])

phonebook["Karol Kurek"] = 343434345
print(phonebook)

phonebook["Alicja Kotowa"] = "Elm Street"
phonebook["Alicja Kotowa"] = 1222132123

print(phonebook)

print(phonebook["Andrew Max"])

#1. Sprawdzić jak otrzymać listę kluczy bądź listę wartości ze słownika
#2. Sprawdzić jakie są inne kolekcje dostępne w Pythonie
#3. Stworzyć słownik (może być uporządkowany), którego wartościami zawsze będą listy liczb, następnie otrzymać listę wartości (czyli listę list) i wyświetlić wszystkie
#elementy z tych wewnętrznych list oraz sumę wszystkich liczbowych wartości
#4. Podobnie słownik zamienić na tuplę