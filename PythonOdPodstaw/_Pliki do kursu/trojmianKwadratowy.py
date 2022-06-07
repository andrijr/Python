#Napisz program rozwiązujący (tzn. obliczający miejsca zerowe) trójmianu kwadratowego, np. 3x^2+5x-20

print("Program obliczy x1 i x2 trójmianu kwadratowego.")
a = float(input("Podaj współczynnik  a: "))
b = float(input("Podaj współczynnik  b: "))
c = float(input("Podaj współczynnik  c: "))

delta = b**2 - 4 * a * c
pierwiastek_z_delty = delta ** 0.5
x1 = (-b-pierwiastek_z_delty)/(2*a)
x2 = (-b+pierwiastek_z_delty)/(2*a)

print("x1:",x1)
print("x2:",x2)