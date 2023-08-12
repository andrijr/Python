print("wyświetlenie cudzysłowu 'tekst' ")
print('wyświetlenie cudzysłowu "tekst" ')


x = int(input("podja liczbę: "))

if x >0:
    print("liczba dodatnia")
elif x == 0:
    print("liczba równa zero")
else:
    print("Liczba ujemna")

# operatoray logiczne
# ==
# >
# <
# >=
# <=
# !=

print("rozwiaż równanie kwadratowe podaj liczby")
a = float(input("Podaj liczbę a rónania kwadratowego: "))
b = float(input("Podaj liczbę b rónania kwadratowego: "))
c = float(input("Podaj liczbę c rónania kwadratowego: "))

delta = b ** 2 - (4 * a * c)
if delta > 0:
    x1 = (- b - (delta ** 0.5)) / (2 * a)
    x2 = (- b + (delta ** 0.5)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
elif delta == 0:
    x = (-b / (2 * a))
    print("x = ", x)
else:
    print("Równanie niema rozwiązania")


print("wyświetlenie cudzysłowu '"' ')
