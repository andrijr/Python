import pickle

from Clock_20_1 import Clock
import pickle as pick # zapisywanie do pliku

zegarek1 = Clock(10, 11, 12)

zegarek1.addTime(2, 150, 50)

print(zegarek1)

# zapisujemy objekt do pliku
file = open("zegarek.objc", 'wb')  # .objc otwieramy obiekt, wb a nie w bo to nie jest string tylko obiekt - prawa do zapisu
# dump() oznacza zrzuć - zapisz plik
pickle.dump(zegarek1, file)
file.close() # kiety robimy open trzeba zrobić close

# odczytujemy zapisany obiekt z pliku
file_pickle = open("zegarek.objc", 'rb') # prawa do zapisu
zegarek = pickle.load(file_pickle)
file_pickle.close()
print(zegarek)

