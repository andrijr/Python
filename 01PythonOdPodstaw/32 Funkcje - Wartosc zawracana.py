
def dodawanie(a, b, c):
    return a + b + c

def mnozenie(a, b, c):
    return a * b * c

def delta(a: float, b: float, c: float):
    return a **2 + 4*a + c




x = float(input("podaj liczbę: "))
y = float(input("podaj liczbę: "))
z = float(input("podaj liczbę: "))


print(dodawanie(x, y, z))
print(dodawanie(1, 2, 3))
print()

suma = dodawanie(x, y, z)
iloczyn = mnozenie(z, y, x)
delta1 = delta(x, y, z)
print(suma)
print(iloczyn)
print(delta1)


# do przetestowania

x, y, z = [float(x) for x in input("Podaj liczbę: ").split()]

suma = dodawanie(x, y, z)
iloczyn = mnozenie(z, y, x)
delt2 = delta(x, y, z)
print(suma)
print(iloczyn)
print(delt2)