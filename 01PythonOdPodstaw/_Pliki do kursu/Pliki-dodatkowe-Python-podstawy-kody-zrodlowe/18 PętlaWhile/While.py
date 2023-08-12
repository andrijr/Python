# x = int(input("Podaj liczbę ujemną: "))
# while x > 0:
#     x = int(input("Podaj liczbę ujemną: "))
#
# print("Dodatnia wartość podanej liczby wynosi: ", -x)

#Gra polega na zgadywaniu przez użytkownika "wymyślonej" przez komputer liczby

liczba = 375
licznik = 1
print("Wylosowałem liczbę z przedziału 1 - 1000. Spróbuj ją zgadnać!")
podana = int(input("Podaj liczbę: "))
while podana != liczba:
    licznik += 1
    if podana > 1000 or podana < 1:
        podana = int(input("Wprowadzona liczba jest spoza przedziału. Spróbuj jeszcze raz: "))
    elif podana > liczba:
        podana = int(input("Wylosowana liczba jest mniejsza. Spróbuj jeszcze raz: "))
    else:
        podana = int(input("Wylosowana liczba jest większa. Spróbuj jeszcze raz: "))

print("Gratuluję! To była liczba", liczba, "Udało ci się zgadnąć za", licznik, "razem.")