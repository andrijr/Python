# sprawdzic czy liczba jest w przedziale (0 - 100) lub obustronnie zamknięta od [200 -300]

value = int(input("podaj liczbę: "))
if (0 < value < 100) or (200 <= value <= 300):
    print("liczba w przydziale", value)
else:
    print("liczba poza przedziałem", value)


if (value >0 and value < 100) or (value >= 200 and value <= 300):
    print("liczba w przydziale", value)
else:
    print("liczba poza przedziałem", value)
