value = int(input("Podaj dowolną liczbę: "))
liczbaDzieliSiePrzez2 = value % 2 == 0
liczbaDzieliSiePrzez3 = value % 3 == 0
liczbaDzieliSiePrzez5 = value % 5 == 0
liczbaDzieliSiePrzez7 = value % 7 == 0

if liczbaDzieliSiePrzez2:
    print("Liczba jest podzielna przez 2")
if liczbaDzieliSiePrzez3:
    print("Liczba jest podzielna przez 3")
if liczbaDzieliSiePrzez5 and liczbaDzieliSiePrzez7:
    print("Liczba jest podzielna przez 35")