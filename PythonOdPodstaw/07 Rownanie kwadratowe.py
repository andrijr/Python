# napisz program obliczający , rozwiązujące miejsca zerowe trójmianu kwadratowego (równania kwadratowego)
# np. 3x**2 + 3x - 20
# napisz program

print("Podaj parametry do rozwiązania równania kwadratowego")
x1 = 0.0
x2 = 0.0
a = float(input("Podaj parametr a: "))
b = float(input("Podaj parametr b: "))
c = float(input("Podaj parametr c: "))
delta = 0.0
delta = (b ** 2) - (4 * a * c)
print("delta równa =:", delta)
if delta > 0 :
    x1 = (- b - (delta ** 0.5)) / (2 * a)
    x2 = (- b + (delta ** 0.5)) / (2 * a)
    print("rozwiązania równania kwadratowego", "x1 =", x1, "x2 =", x2)
elif delta == 0 :
    x1 = - b  / (2 * a)
    print("rozwiązania równania kwadratowego", "x1 = ", x1)
else :
    print("brak rozwiązań równania kwadratowego")

