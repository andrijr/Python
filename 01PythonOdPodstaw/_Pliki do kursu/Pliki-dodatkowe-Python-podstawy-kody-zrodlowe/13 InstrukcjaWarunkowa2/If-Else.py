# x = int(input("Podaj liczbę: "))
# if x > 0:
#     print("x jest dodatni")
# elif x == 0:
#     print("x nie jest dodatni i nie jest ujemny")
# else:
#     print("x jest ujemny")

# == - sprawdzenie czy lewa strona równa się prawej
# = - przypisanie lewej stronie, prawą
# > - sprawdzenie czy lewa strona jest większa od prawej
# < - sprawdzenie czy lewa strona jest mniejsza od prawej
# >= - sprawdzenie czy lewa strona jest większa bądź jest równa prawej
# <= - sprawdzenie czy lewa strona jest mniejsza bądź jest równa prawej
# != - sprawdzenie czy strony są różne

wspolczynnikA = int(input("Podaj współczynnik a równania kwadratowego: "))
wspolczynnikB = int(input("Podaj współczynnik b równania kwadratowego: "))
wspolczynnikC = int(input("Podaj współczynnik c równania kwadratowego: "))

delta = wspolczynnikB*wspolczynnikB - 4 * wspolczynnikA * wspolczynnikC

if delta > 0:
    x1 = (-wspolczynnikB - delta**0.5)/2
    x2 = (-wspolczynnikB + delta**0.5)/2
    print("Pierwiastki równania kwadratowego to x1 =", x1, "oraz x2 =", x2)
elif delta == 0:
    x0 = -wspolczynnikB/2
    print("Jedyny pierwiastek równania kwadratowego to x0 =", x0)
else:
    print("Równanie nie ma pierwiastków!")

