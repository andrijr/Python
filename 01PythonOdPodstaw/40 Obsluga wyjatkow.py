
try:
    zmienna = int(input("Podaj liczbę: "))
except:
    print("to nie jest liczba")


try:
    file = open('39_plik_tekstowy.txt', 'r+')
    print(file.read())
    file.close()
except:
    print('plik nie istnieje')