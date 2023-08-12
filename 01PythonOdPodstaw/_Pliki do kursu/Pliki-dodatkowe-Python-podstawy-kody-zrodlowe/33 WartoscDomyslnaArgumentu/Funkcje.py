def srednia(listaLiczb: list, listaWag = []):
    wynik = 0
    for x in listaLiczb:
        wynik += x*waga
    return wynik/(waga*len(listaLiczb))

lista = []
x = float(input("Podaj liczbę do dodania. Jeżeli chcesz zakończyć wpisz 0: "))
while x != 0:
    lista.append(x)
    x = float(input("Podaj liczbę do dodania. Jeżeli chcesz zakończyć wpisz 0: "))

print("Średnia tych liczb wynosi: ", srednia(lista,5))