
import pickle

from Clock_20_1 import Clock
import pickle as pick # zapisywanie do pliku

zegarek1 = Clock(10, 11, 12)

# zapisujemy objekt do pliku
try:
    file = open("zegarek.objc", 'wb')  # .objc otwieramy obiekt, wb a nie w bo to nie jest string tylko obiekt - prawa do zapisu
    pickle.dump(zegarek1, file) # dump() oznacza zrzuć - zapisz plik
    print("Nie można było utworzyć pliku pod czas zapisu")
    file.close() # kiety robimy open trzeba zrobić close
except IOError:
    print("Nie można było utworzyć pliku na dysku")


try:
    file2 = open("zegarek.objc", 'wb')
    try:
        pickle.dump(zegarek1, file2)
    except:
        print("Nie można było utworzyć pliku pod czas zapisu")
    file2.close()
except IOError:
    print("Nie można było utworzyć pliku na dysku")


try:
    file2 = open("zegarek.objc", 'wb')
    try:
        pickle.dump(zegarek1, file2)
    except:
        print("Nie można było utworzyć pliku pod czas zapisu")
    finally: # finally wykonuję się zawsze nie zależnie czy try będzie tru czy false
        file2.close()
except IOError:
    print("Nie można było utworzyć pliku na dysku")


# skrót do try: except: finally przy zapisywaniu pliku:
#     with open("zegarek.objc", 'wb') as file2
#         pickle.dump(zegarek1,file2)

try:
    with open("Zegarek.objc",'wb') as file2:
        pick.dump(zegarek1,file2)
except IOError:
    print("Nie można było utworzyć pliku na dysku")


# odczytujemy zapisany obiekt z pliku
with open("zegarek.objc", 'rb') as file_pickle:
    zegarek = pickle.load(file_pickle)

print(zegarek)
