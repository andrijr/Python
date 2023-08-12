try:
    file = open("plik_przykladowy.txt",'r', encoding="utf8")
    file.close()
except:
    print("Plik nie istnieje!")