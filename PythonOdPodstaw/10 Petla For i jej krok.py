suma = 0
for x in range(0, 1000,5):
    suma += x
print(suma)


for x in range(1,10, 3):
    print(x)

# program oblicza średną aretmetyczną dowolnej ilości liczb

ileLiczb = int(input("podaj z ilu liczb średnia"))
suma = 0
for x in range(0, ileLiczb):
    suma += float(input("Podaj liczbę: "))
sredniaAretmetyczna = suma / x
print(sredniaAretmetyczna)

ileliczb = int(input("podaj z ile liczb średnia: "))
suma = 0
x = 0
for i in range(0, ileliczb):
    x = float(input("podja liczbę: "))
    suma += x
wynik = suma / ileliczb
print(suma)
print(wynik)
