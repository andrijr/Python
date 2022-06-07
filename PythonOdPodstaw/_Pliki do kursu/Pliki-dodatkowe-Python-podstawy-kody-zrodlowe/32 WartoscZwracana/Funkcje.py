def dodaj(a,b,c):
    return a + b + c

def pomnoz(a,b,c):
    return a * b * c

def delta(a: float, b: float, c: float):
    return b**2 - 4 * a * c

x, y, z = [float(x) for x in input("Podaj trzy liczby oddzielone spacjami: ").split()]

suma = dodaj(x,y,z)
iloczyn = pomnoz(x,y,z)
wynikDelty = delta(x,y,z)

print("Wynik dodawania to:", suma)
print("Wynik mnożenia to:", iloczyn)
print("Zaś delta wynosi :", wynikDelty)

x, y, z = [float(x) for x in input("Podaj trzy liczby oddzielone spacjami: ").split()]

suma = dodaj(x,y,z)
iloczyn = pomnoz(x,y,z)
wynikDelty = delta(x,y,z)

print("Wynik dodawania to:", suma)
print("Wynik mnożenia to:", iloczyn)
print("Zaś delta wynosi :", wynikDelty)