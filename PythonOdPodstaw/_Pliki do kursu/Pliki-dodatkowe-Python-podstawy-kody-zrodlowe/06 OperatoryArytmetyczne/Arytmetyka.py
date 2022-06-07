import math

liczba1 = 5
liczba2 = 31
liczba3 = 36

# Obliczenia
suma = liczba1 + liczba2
roznica = liczba1 - liczba2
iloczyn = liczba1 * liczba2
iloraz = liczba1 / liczba2
potegowanie = liczba1 ** liczba2
ilorazCalkowity = liczba2 // liczba1
reszta = liczba2 % liczba1
pierwiastek = liczba3 ** 0.5 # pierwiastkowanie stopnia drugiego to podnoszenie do potęgi 1/2 czyli 0.5
pierwiastek2 = math.sqrt(liczba3) # inny sposób pierwiastkowania

# Wyświetlanie
print(suma)
print(roznica)
print(iloczyn)
print(iloraz)
print(potegowanie)
print(ilorazCalkowity)
print(reszta)
print("Wynik dzielenia", liczba2, "przez", liczba1, "to:", ilorazCalkowity, "całych i reszty", reszta)
print(math.floor(pierwiastek))
print(pierwiastek2)