for x in range(0,10,2):
    print(x)

print("----")
for x in range(0,100,5):
    print(x)

print("----")
suma = 0
iloczyn = 1
for x in range(1,100,5):
    print(x)
    suma += x
    iloczyn *= x
print(suma)
print(iloczyn)

# policz średnią aretmetyczna liczby naturalnej
ileliczb = int(input("podaj z ili liczb chcesz policzyć srednią: "))
suma = 0
for x in range(0,ileliczb):
    liczba = float(input("podaj liczbę: "))
    suma += liczba
suma = suma / liczba
print("średnia wynosi: ", suma)