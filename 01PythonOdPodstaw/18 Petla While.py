
# x = int(input("podaj liczbę ujemnę: "))
# while x > 0:
#     x = int(input("Spróbój ponownie: "))
# print("wprowadzona liczbą", x)

# zgadywanie przez urzytkownika wymyślonej przez komputer liczbę

print("wylosowana liczba z przeedziału od 1 do 1000")
liczba = 375
licznik = 1
x = int(input("podaj liczbę: "))
while x != liczba:
    licznik += 1
    if liczba < x <= 1000:
        x = int(input("Spróbój ponownie liczba jest mniejsza: "))
    elif 0 < x <= liczba:
        x = int(input("Spróbój ponownie liczba jest większa: "))
    else:
        x = int(input("liczba poza zakresem podaj liczbę: "))
print("zgadleś liczbę", x , "za ", licznik, "razem")