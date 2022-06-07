
#gra polegająca na zgadywaniu wymyślonej przez komputer liczby

min = 1
max = 1000
liczba = 375
licznk = 0
liczbaWprowadzona = int(input("Podaj Liczbę: "))
while liczbaWprowadzona != liczba:
    licznk +=1
    if liczbaWprowadzona > max or liczbaWprowadzona < min:
        print("Liczba", liczbaWprowadzona,  "jest z posza przedziału", "od", min, "do", max)
    elif liczbaWprowadzona > liczba:
        print("Liczba", liczbaWprowadzona,  "jest większa od szukanej liczby")
    else:
        print("Liczba", liczbaWprowadzona, "jest mniejsza od szukanej liczby")
    liczbaWprowadzona = int(input("Podana liczba błędna spróbój jeszcze raz: "))
print("Liczba jest odgadnięta i jest równa: ", liczbaWprowadzona)
print("ogadłeś za ", licznk, "razem")